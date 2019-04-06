var Set1Valid = 0;
var Set2Valid = 0;
var Set3Valid = 1;
var winner1 = 0;
var winner2 = 0;
var winner3= 0;

function ValidSet1() {
  var x, text, p1s1, p2s1;

  // Get the value of the input field with id="numb"
  p1s1 = document.getElementById("p1s1").value;
  p2s1 = document.getElementById("p2s1").value;

  // If x is Not a Number or less than one or greater than 10
  if (isNaN(p1s1) || isNaN(p2s1)) {
    text = "Geen geldige score";
    var Set1Valid = 0;
  } else if (p1s1 == p2s1) {
    text = "Geen geldige score";
    var Set1Valid = 0;
  } else if (p1s1 < 21  & p2s1 < 21 ) {
    text = "Geen geldige score";
    var Set1Valid = 0;
  } else if (p1s1 == 21  & p2s1 == 20 ) {
    text = "Geen geldige score";
    var Set1Valid = 0;
  } else if (p2s1 == 21  & p1s1 == 20 ) {
    text = "Geen geldige score";
    var Set1Valid = 0;
  } else if (p1s1 > 21  || p2s1 > 21 ) {
    if (((p1s1 - p2s1) != 2) & ((p2s1 - p1s1) != 2)) {
        text = "Geen geldige score";
        var Set1Valid = 0;
    } else {
        text = "";
        var Set1Valid = 1;
    }
  } else {
    text = "";
  }
  if (p1s1 > p2s1) {
      winner1 = 1;
  } else {
      winner1 = 2;
  }
  document.getElementById("ValidationSet1").innerHTML = text;
}

function ValidSet2() {
  var x, text, p1s2, p2s2;

  // Get the value of the input field with id="numb"
  p1s2 = document.getElementById("p1s2").value;
  p2s2 = document.getElementById("p2s2").value;

  // If x is Not a Number or less than one or greater than 10
  if (isNaN(p1s2) || isNaN(p2s2)) {
    text = "Geen geldige score";
    var Set2Valid = 0;
  } else if (p1s2 == p2s2) {
    text = "Geen geldige score";
    var Set2Valid = 0;
  } else if (p1s2 < 21  & p2s2 < 21 ) {
    text = "Geen geldige score";
    var Set2Valid = 0;
  } else if (p1s2 == 21  & p2s2 == 20 ) {
    text = "Geen geldige score";
    var Set2Valid = 0;
  } else if (p2s2 == 21  & p1s2 == 20 ) {
    text = "Geen geldige score";
    var Set2Valid = 0;
  } else if (p1s2 > 21  || p2s2 > 21 ) {
    if (((p1s2 - p2s2) != 2) & ((p2s2 - p1s2) != 2)) {
        text = "Geen geldige score";
        var Set2Valid = 0;
    } else {
        text = "";
        var Set2Valid = 1;
    }
  } else {
    text = "";
  }
  document.getElementById("ValidationSet2").innerHTML = text;
  if (p1s2 > p2s2) {
      winner1 = 1;
  } else {
      winner1 = 2;
  }
}

function ValidSet3() {
  var x, text, p1s3, p2s3;

  // Get the value of the input field with id="numb"
  p1s3 = document.getElementById("p1s3").value;
  p2s3 = document.getElementById("p2s3").value;

  // If x is Not a Number or less than one or greater than 10
  if (isNaN(p1s3) || isNaN(p2s3)) {
    text = "Geen geldige score";
    var Set3Valid = 0;
  } else if (p1s3 == p2s3) {
    text = "Geen geldige score";
    var Set3Valid = 0;
  } else if (p1s3 < 21  & p2s3 < 21 ) {
    text = "Geen geldige score";
    var Set3Valid = 0;
  } else if (p1s3 == 21  & p2s3 == 20 ) {
    text = "Geen geldige score";
    var Set3Valid = 0;
  } else if (p2s3 == 21  & p1s3 == 20 ) {
    text = "Geen geldige score";
    var Set3Valid = 0;
  } else if (p1s3 > 21  || p2s3 > 21 ) {
    if (((p1s3 - p2s3) != 2) & ((p2s3 - p1s3) != 2)) {
        text = "Geen geldige score";
        var Set3Valid = 0;
    } else {
        text = "";
        var Set3Valid = 1;
    }
  } else {
    text = "";
  }
   if (p1s3 > p2s3) {
      winner1 = 1;
  } else {
      winner1 = 2;
  }
  document.getElementById("ValidationSet3").innerHTML = text;
}

function ValidateMatch() {
    if (Set3Valid != 1 || Set2Valid != 1 || Set1Valid != 1 ) {
        alert("Check de ingevulde scores.");
        return false;
    }
}