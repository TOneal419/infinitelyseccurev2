/*! For license information please see main.js.LICENSE.txt */
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
