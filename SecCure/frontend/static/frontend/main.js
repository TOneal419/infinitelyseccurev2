/*! For license information please see main.js.LICENSE.txt */
// (window).scroll(function() {
//     if ($(this).scrollTop() >= 80) {        
//         $('#return-to-top').fadeIn(200);    
//     } else {
//         $('#return-to-top').fadeOut(200);   
//     }
// });
// ('#return-to-top').onclick(function() {      
//     ('body,html').animate({
//         scrollTop : 0                       
//     }, 500);
// });

function playAudio(value) {
    var audio = document.getElementById(String(value));
    audio.play();
    //var audio = new Audio(String(value));
    //audio.play();
  }
function pauseAudio(value) {
    var audio = document.getElementById(String(value));
    audio.pause();
  }
function submitForm() {
    //let form = document.getElementById("form_vt");
    //document.getElementById("vtoutput").innerHTML = form.submit().innerHTML;
    var http = new XMLHttpRequest();
    http.open("POST", "api/vt", true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var params = "Url=" + document.getElementById('vtinput').value ;
    http.send(params);
    http.onload = function() {
      const myObj = JSON.parse(http.responseText)
      var printable = "Time Submitted: " + myObj.submitted + "<br>";
      var harmless = ":        ";
      var malicious = "";
      var suspicious = "";
      var undetected = "";
      var timeout = "";
      for (var key in myObj.Data) {
        
        if (myObj.Data[key].category == "harmless"){
          harmless +=  String(key) + ", ";
        } 
        if (myObj.Data[key].category == "malicious") {
          malicious += ": " + String(key) + ",    Reason: " + String(myObj.Data[key].result) + "<br>"
        }// else 
        if (myObj.Data[key].category == "suspicious" ) {
          suspicious += String(key) + ", "
        } //else if (myObj.Data[key].category == "undetected") {
          //undetected +=  "----" + String (key) + "<br>"
      //  } else {
        //  timeout += "----" String(key) + "<br>"
       // }
      }
      var printable1 = printable + "<br>";
      printable1 +=  String(myObj.Stats.harmless) + " Search Engines that Found this URL harmless <br>" + harmless + "<br><br>";
      printable1 +=  String(myObj.Stats.malicious) + " Search Engines Found this URL malicious <br> " + malicious + "<br><br>";
      printable1 += String(myObj.Stats.suspicious) + " Search Engines Fount this URl suspicious <br> " + suspicious + "<br><br>";
      printable1 += String(myObj.Stats.undetected) + " Search Engines were Unable to Detect the URL <br> " + undetected + "<br><br>";
      printable1 += String(myObj.Stats.timeout) + " Search Engines Timed out " + timeout + "<br><br>";
      //JSON.stringify(http.responseText);
      document.getElementById('vtoutput').innerHTML = printable1;
      var https = new XMLHttpRequest();
        https.open("POST", "api/tts", true);
        https.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        var hold = document.getElementById('vtoutput');
        if (String(hold.innerHTML) == "undefined") {
          hold = "No Content";
        } 
        var params = "filename=VT/results" +"&scripts=" + String(hold.textContent || hold.innerText) ;
        https.send(params);
    }
}
function submitForm1() {
    //let form = document.getElementById("form_vt");
    //document.getElementById("vtoutput").innerHTML = form.submit().innerHTML;
    var http = new XMLHttpRequest();
    
    http.open("POST", "api/pwn", true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var params = "domainname=" + document.getElementById('pwninput').value ;
    http.send(params);
    http.onload = function() {
      const myObj = JSON.parse(http.responseText)[0]
      var res = "On " + String(myObj.BreachDate) +" the domain " + String(myObj.Domain) + " was breached" 
      res += ". " + String(myObj.Description);
      if (String(myObj.Name) == "Not Detected") {
        res = "The domain " + String(myObj.Domain) + " was not found in the database."
      }
      document.getElementById('pwnoutput').innerHTML = res;
      // finished with hibp now creating audio
      var https = new XMLHttpRequest();
        https.open("POST", "api/tts", true);
        https.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        var hold = document.getElementById('pwnoutput');
        if (String(hold.innerHTML) == "undefined") {
          hold = "No Content";
        } 
        var params = "filename=result" +"&scripts=" + String(hold.textContent || hold.innerText) ;
        https.send(params);
        
    }
}

function darkMode() {
    const darkModeSwitch = document.getElementById('checkbox');

    darkModeSwitch.addEventListener('change',() => {   
        alert("darkmode works");
        document.body.classList.toggle('dark');
        var theme = document.body.classList.contains('dark') ? 'dark' : 'light';
        localStorage.setItem("theme", theme);
    });
}

function themeStatus() {
    alert("themestatus works");
    const darkModeSwitch = document.getElementById('checkbox');
    var currentTheme = localStorage.getItem("theme");
    if(currentTheme === 'dark'){
        darkModeSwitch.click();
    }
}

