var Set1Valid = 0;
var Set2Valid = 0;
var Set3Valid = 1;
var winner1 = 0;
var winner2 = 0;
var winner3 = 0;

function ValidSet1() {
  var text, p1s1, p2s1;

  p1s1 = document.getElementById("p1s1").value;
  p2s1 = document.getElementById("p2s1").value;

  if (isNaN(p1s1) || isNaN(p2s1)) {
    Set1Valid = 0;
  } else if (p1s1 == p2s1) {
    Set1Valid = 0;
  } else if ( p1s1 < 0 || p2s1 < 0) {
    Set1Valid = 0;
  } else if (p1s1 < 21  & p2s1 < 21 ) {
    Set1Valid = 0;
  } else if (p1s1 == 21  & p2s1 == 20 ) {
    Set1Valid = 0;
  } else if (p2s1 == 21  & p1s1 == 20 ) {
    Set1Valid = 0;
  } else if (p1s1 > 21  || p2s1 > 21 ) {
    if (((p1s1 - p2s1) != 2) & ((p2s1 - p1s1) != 2)) {
        Set1Valid = 0;
    } else {
        Set1Valid = 1;
    }
  } else if (p1s1 != null & p2s1 != null)  {
    Set1Valid = 1;
  } else{
    Set1Valid = 0;
  }

  if ((p1s1 > p2s1) & Set1Valid == 1) {
      winner1 = 1;
  } else if ((p1s1 < p2s1) & Set1Valid == 1) {
      winner1 = 2;
  }

  if (winner1 != winner2 & Set1Valid == 1 & Set2Valid == 1) {
      document.getElementById("set3").style.display = "table-row-group";
  }  else {
    document.getElementById("set3").style.display = "none";
    document.getElementById("p1s3").value = "0";
    document.getElementById("p2s3").value = "0";
    Set3Valid = 1;
  }


  if (Set1Valid == 1 & p1s1 != null & p2s1 != null) {
    text = "✓";
    document.getElementById("ValidationSet1").className = "text-success";
  }
  else {
    text = "Geen geldige score";
    document.getElementById("ValidationSet1").className = "text-danger";
  }
  document.getElementById("ValidationSet1").innerHTML = text;
}

function ValidSet2() {
  var text, p1s2, p2s2;

  p1s2 = document.getElementById("p1s2").value;
  p2s2 = document.getElementById("p2s2").value;

  if (isNaN(p1s2) || isNaN(p2s2)) {
    Set2Valid = 0;
  } else if (p1s2 == p2s2) {
    Set2Valid = 0;
  } else if ( p1s2 < 0 || p2s2 < 0) {
    Set2Valid = 0;
  } else if (p1s2 < 21  & p2s2 < 21 ) {
    Set2Valid = 0;
  } else if (p1s2 == 21  & p2s2 == 20 ) {
    Set2Valid = 0;
  } else if (p2s2 == 21  & p1s2 == 20 ) {
    Set2Valid = 0;
  } else if (p1s2 > 21  || p2s2 > 21 ) {
    if (((p1s2 - p2s2) != 2) & ((p2s2 - p1s2) != 2)) {
        Set2Valid = 0;
    } else {
        Set2Valid = 1;
    }
  } else if (p1s2 != null & p2s2 != null) {
    Set2Valid = 1;
  } else {
    Set2Valid = 0;
  }

  if ((p1s2 > p2s2) & Set2Valid == 1) {
      winner2 = 1;
  } else if ((p1s2 < p2s2) & Set2Valid == 1) {
      winner2 = 2;
  }

  if (winner1 != winner2 & Set2Valid == 1 & Set1Valid == 1) {
      document.getElementById("set3").style.display = "table-row-group";
  }  else {
    document.getElementById("set3").style.display = "none";
    document.getElementById("p1s3").value = "0";
    document.getElementById("p2s3").value = "0";
    Set3Valid = 1;
  }

  if (Set2Valid == 1 & p1s2 != null & p2s2 != null) {
    text = "✓";
    document.getElementById("ValidationSet2").className = "text-success";
  }
  else {
    text = "Geen geldige score";
    document.getElementById("ValidationSet2").className = "text-danger";
  }
  document.getElementById("ValidationSet2").innerHTML = text;
}

function ValidSet3() {
  var text, p1s3, p2s3;

  p1s3 = document.getElementById("p1s3").value;
  p2s3 = document.getElementById("p2s3").value;

  if (isNaN(p1s3) || isNaN(p2s3)) {
    Set3Valid = 0;
  } else if (p1s3 == p2s3) {
    Set3Valid = 0;
  } else if ( p1s3 < 0 || p2s3 < 0) {
    Set3Valid = 0;
  } else if (p1s3 < 21  & p2s3 < 21 ) {
    Set3Valid = 0;
  } else if (p1s3 == 21  & p2s3 == 20 ) {
    Set3Valid = 0;
  } else if (p2s3 == 21  & p1s3 == 20 ) {
    Set3Valid = 0;
  } else if (p1s3 > 21  || p2s3 > 21 ) {
    if (((p1s3 - p2s3) != 2) & ((p2s3 - p1s3) != 2)) {
        Set3Valid = 0;
    } else {
        Set3Valid = 1;
    }
  } else if (p1s3 != null & p2s3 != null) {
    Set3Valid = 1;
  } else {
    Set3Valid = 0;
  }

  if ((p1s3 > p2s3) & Set3Valid == 1) {
      winner3 = 1;
  } else if ((p1s3 < p2s3) & Set3Valid == 1) {
      winner3 = 2;
  }

  if (Set3Valid == 1 & p1s3 != null & p2s3 != null) {
    text = "✓";
    document.getElementById("ValidationSet3").className = "text-success";
  }
  else {
    text = "Geen geldige score";
    document.getElementById("ValidationSet3").className = "text-danger";
  }
  document.getElementById("ValidationSet3").innerHTML = text;
}

function ValidateMatch() {
    if (Set3Valid != 1 || Set2Valid != 1 || Set1Valid != 1 ) {
        alert("Check de ingevulde scores.");
        event.preventDefault();
        returnToPreviousPage();
        return false;
    } else {
      return true;
    }
}
