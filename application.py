import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, GenMatch


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set DB to use Heroku Postgres database
db = SQL("""postgres://ppaikjrazrltwg:d7b4bbbaa8d1470e42a97e2d58a4d7ba752d007ecfc85d67daf913a8284c3421@ec2-46-137-121-216.eu-west-1.compute.amazonaws.com:5432/df5rrijrug19j9
""")

#Generate indexpage with personalized welcome text and current rankings
@app.route("/")
@login_required
def index():
    #SELECT username
    username = db.execute("SELECT username FROM users where id=:id", id=session.get("user_id"))
    #SELECT all users information and render index page(klassement)
    ranking = db.execute(""" SELECT username, id, won, lost, (won - lost) AS balance
                               FROM users WHERE active = 1 ORDER BY balance DESC """)
    return render_template("index.html", username=username, ranking=ranking)

#Function the check username
@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    return jsonify("TODO")

#Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        # Query database for username
        rows = db.execute("""SELECT username, id, userlevel, active, hash
                               FROM users WHERE lower(username) = :username""",
                          username = str.lower(request.form.get("username")))
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)
        # Remember which user has logged in and acceslevel of user
        session["user_id"] = rows[0]["id"]
        session["userlevel"] = rows[0]["userlevel"]
        session["active"] = rows[0]["active"]
        # Redirect user to home page
        return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

#Logout Function
@app.route("/logout")
def logout():
    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/")

#Register Function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #Check for username
        if not request.form.get("username"):
            return apology("must provide username", 400)
        #Check for password
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        #Check for repeated password
        elif not request.form.get("confirmation"):
            return apology("must repeat password", 400)
        #Check Passwords for mismatch
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match", 400)
        # Query database for username
        checkname = db.execute("SELECT * FROM users WHERE lower(username) = :username",
                          username=str.lower(request.form.get("username")))
        # Ensure username not yet exists
        if len(checkname) == 1:
            return apology("username already exists", 400)
        # Insert user into database USERS
        else:
            db.execute("""INSERT INTO users (username, hash) VALUES (:username, :hash)""",
                       username = request.form.get("username"),
                       hash = generate_password_hash(request.form.get("password")))
            # Login the user and generate matches
            UserSessionInfo = db.execute("""SELECT id, userlevel, active FROM users WHERE username = :username""",
                                 username=request.form.get("username"))
            #Set all session info
            session["user_id"] = UserSessionInfo[0]["id"]
            session["user_level"] = UserSessionInfo[0]["userlevel"]
            session["active"] = UserSessionInfo[0]["active"]
            return redirect("/")
    # when method is not POST
    else:
        return render_template("register.html")

#Funtion for game input
@app.route("/input", methods=["GET", "POST"])
@login_required
def input():
    username = db.execute("SELECT username FROM users where id=:id", id=session.get("user_id"))
    username = username[0]["username"]
    if request.method== "POST":
        #Check for earlier match-ups
        CheckEarlyComp = db.execute("SELECT idplayerone, idplayertwo FROM games WHERE (idplayerone = :id1 AND idplayertwo = :id2) OR (idplayerone = :id2 AND idplayertwo = :id1)", id1=session.get("user_id"), id2=request.form.get("opid"))
        if len(CheckEarlyComp) >= 1:
            return apology("Je speelde reeds tegen deze tegenstander", 69)
        else:
            GameSets = ["p1s1","p2s1","p1s2","p2s2","p1s3","p2s3",]
            GameResults = []
            counter = 0
            for i in GameSets:
                FormGrab = request.form.get(i)
                if not FormGrab:
                    FormGrab = 0
                GameResults.append(FormGrab)
                counter += 1
            setsone = 0
            setstwo = 0
            for i in range (0, 6, 2):
                print (i)
                if int(GameResults[i]) > int(GameResults[i+1]):
                    print (GameResults[i], ">", GameResults[i+1])
                    setsone += 1
                    print (i)
                    print ("set", i, "wordt gewonnen door speler 1 met:",GameResults[i], GameResults[i+1] )
                print (i)
                if int(GameResults[i]) < int(GameResults[i+1]):
                    print (GameResults[i], "<", GameResults[i+1])
                    setstwo += 1
                    print (i)
                    print ("set", i, "wordt gewonnen door speler 2 met:",GameResults[i], GameResults[i+1] )
            matchinfo = db.execute("""SELECT idplayerone, idplayertwo FROM games WHERE matchid=:matchid""",
                                      matchid = request.form.get("match"))
            if setsone > setstwo:
                winner = matchinfo[0]["idplayerone"]
                loser = matchinfo[0]["idplayertwo"]
                print ( winner, "wint tegen", loser, "met",setsone,"-", setstwo)
            elif setsone < setstwo:
                winner = matchinfo[0]["idplayertwo"]
                loser = matchinfo[0]["idplayerone"]
                print ( winner, "wint tegen", loser, "met",setstwo,"-", setsone)
            else:
                return apology("Er liep iets mis! Heb je alle scores correct ingevuld? Probeer het opnieuw.", 69)
            print (GameResults, setsone, setstwo, matchinfo[0]["idplayerone"], matchinfo[0]["idplayertwo"], winner, loser)
            db.execute("""UPDATE games
                             SET winnerid=:winnerid, p1s1=:p1s1, p1s2=:p1s2, p1s3=:p1s3,
                                 p2s1=:p2s1, p2s2=:p2s2, p2s3=:p2s3, time=now()::timestamptz(0)
                           WHERE matchid = :matchid""",
                           winnerid=winner,
                           p1s1=GameResults[0], p1s2=GameResults[2], p1s3=GameResults[4],
                           p2s1=GameResults[1], p2s2=GameResults[3], p2s3=GameResults[5],
                           matchid = request.form.get("match"))
            # update wins and odds
            db.execute("UPDATE users SET won = won + 1, odds = odds - 5 WHERE id=:id", id=winner)
            db.execute("UPDATE users SET lost = lost + 1, odds = odds + 5 WHERE id=:id", id=loser)
        return redirect("/")
    # If method is not POST
    else:
        UnplayedGames = db.execute("""
                   SELECT g.idplayerone, g.idplayertwo, g.matchid,
                          p1.username playone,
                          p2.username playtwo
                     FROM games g
                     JOIN users p1 ON g.idplayerone = p1.id
                     JOIN users p2 ON g.idplayertwo = p2.id
                     WHERE (g.idplayerone = :id OR g.idplayertwo = :id)  AND g.winnerid IS NULL
                     """, id=session.get("user_id"))
        if len(UnplayedGames) == 0:
            return apology("Er zijn op dit moment geen wedstrijden voor jou. kom later nog eens terug.")
        else:
            return render_template("input.html", UnplayedGames=UnplayedGames)

@app.route("/history", methods=["GET"])
@login_required
def history():
    #Grab 20 most recent played games
    PlayedGames = db.execute("""
           SELECT g.idplayerone, g.idplayertwo, g.matchid, g.winnerid, g.time,
                  g.p1s1, g.p1s2, g.p1s3, g.p2s1, g.p2s2, g.p2s3,
                  p1.username playone,
                  p2.username playtwo
             FROM games g
             JOIN users p1 ON g.idplayerone = p1.id
             JOIN users p2 ON g.idplayertwo = p2.id
             WHERE g.winnerid IS NOT NULL
         ORDER BY g.time
            LIMIT 20
        """)
    return render_template("history.html", PlayedGames=PlayedGames)

@app.route("/user/<int:id>")
@login_required
def userpage(id):
    userinfo = db.execute(""" SELECT username, won, lost, odds, cash FROM users WHERE id=:id""", id=id)
    userhistory = db.execute("""
           SELECT g.idplayerone, g.idplayertwo, g.matchid, g.winnerid, g.time,
                  p1.username playone,
                  p2.username playtwo
             FROM games g
       INNER JOIN users p1 ON g.idplayerone = p1.id
       INNER JOIN users p2 ON g.idplayertwo = p2.id
             WHERE g.idplayerone = :id or g.idplayertwo = :id
         ORDER BY g.time DESC
        """, id=id)
    return render_template("user.html", userhistory=userhistory, userinfo=userinfo)

@app.route("/activate", methods=["GET", "POST"])
@login_required
def activate():
    if request.method == "POST":
        KeyValidation = db.execute("SELECT key FROM keys WHERE key=:key", key = request.form.get("key"))
        if len(KeyValidation) == 0:
            return apology("Dit is geen geldige code, probeer het opnieuw.")
        else:
            db.execute("DELETE FROM keys WHERE key =:key", key = request.form.get("key"))
            db.execute("UPDATE users SET active = 1 WHERE id=:id", id = session.get("user_id"))
            CheckActivation = db.execute("SELECT active FROM users WHERE id=:id", id = session.get("user_id"))
            session["active"] = CheckActivation[0]["active"]
            userid = session.get("user_id")
            GenMatch(userid, db=db)
            return apology("Je bent succesvol ingeschreven.")
    else:
        return render_template("activate.html")

@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    if request.method == "POST":
        KeyForm = request.form.get("NewKey")
        if KeyForm:
            db.execute("INSERT INTO keys VALUES (:key)", key=KeyForm)
        keys = db.execute("SELECT * FROM keys")
        return render_template("admin.html", keys=keys)
    else:
        keys = db.execute("SELECT * FROM keys")
        return render_template("admin.html", keys=keys)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
