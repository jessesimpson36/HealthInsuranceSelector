
// source for base javascript for multi-form page.
// https://www.w3schools.com/howto/howto_js_form_steps.asp?
var currentTab = 0; // Current tab is set to be the first tab (0)
// Display the crurrent tab
window.onload = function () { showTab(0); }

function showTab(n) {
  // This function will display the specified tab of the form...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  for( var i = 0; i < x.length; i++){
    if (i != n){
      x[i].style.display = "none";
    }
  }
  //... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  //... and run a function that will display the correct step indicator:
  fixStepIndicator(n)
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form...
  if (currentTab >= x.length) {
    // ... the form gets submitted:
    document.getElementById("regForm").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByClassName("required");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false
      valid = false;
    }
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid; // return the valid status
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class on the current step:
  x[n].className += " active";
}


// Load google charts
//google.charts.load('current', {'packages':['corechart']});
//google.charts.setOnLoadCallback(drawChart);
//
//// Draw the chart and set the chart values
//function drawChart(pos_count, neg_count, high_count, low_count) {
//  var data = google.visualization.arrayToDataTable([
//  ['Type', 'Reviews'],
//  ['Positive Count', pos_count],
//  ['Negative Count', neg_count],
//  ['High Count', high_count],
//  ['Low Count', low_count]
//]);
//
//// Optional; add a title and set the width and height of the chart
//  var options = {'title':'Reviews', 'width':400, 'height':300};
//
//  // Display the chart inside the <div> element with id="piechart"
//  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
//  chart.draw(data, options);
//  drawChart({{ resultsObj.pos_count }}, {{ resultsObj.neg_count }}, {{ resultsObj.high_count }}, {{ resultsObj.low_count }});



