
// source for base javascript for multi-form page.
// https://www.w3schools.com/howto/howto_js_form_steps.asp?
var currentTab = 0; // Current tab is set to be the first tab (0)
// Display the crurrent tab
window.onload = function () { showTab(0); showTobaccoQuestion(); showListOfBenefits(); }

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

function showTobaccoQuestion(){
    var x = document.getElementById("smokeBox").checked;
    var tobaccoLabel = document.getElementById("tobaccoLabel");
    var tobaccoInput = document.getElementById("tobaccoInput");
    if (x){
        tobaccoInput.style.display = "inline";
        tobaccoLabel.style.display = "inline";
    } else {
        tobaccoInput.style.display = "none";
        tobaccoLabel.style.display = "none";
    }
}


function showListOfBenefits(){
    var x = document.getElementById("benefitsCheckBox").checked;
    var listOfBenefits = document.getElementById("benefitsSelect");
    var benefitsLabel = document.getElementById("benefitsLabel")
    if ( x ){
        listOfBenefits.style.display = "inline";
        benefitsLabel.style.display = "inline"
    } else {

        listOfBenefits.style.display = "none";
        benefitsLabel.style.display = "none";
    }
}

function getResults(){
    $.ajax({
        url:'/get_results/',
        type: "GET",
        success:function(response){},
        complete:function(){},
        error:function (xhr, textStatus, thrownError){}
    });

});
}