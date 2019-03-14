import requests
import urllib.parse

from cs50 import SQL
from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=message), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

#Function to create match-ups for current user, matches with all excisting users
def GenMatch(user, db):
	#grab all users
	opponents = db.execute("""
							   SELECT id
							     FROM users
								WHERE id != :user AND active = 1
								""", user = user)
	# Generate the matches and put them in database
	for opponent in opponents:
		db.execute("""
					INSERT into games (idplayerone, idplayertwo) VALUES (:user, :opponent)
					""", user = user, opponent = opponent["id"])
		print ( "entering",user,"vs",opponent["id"])
