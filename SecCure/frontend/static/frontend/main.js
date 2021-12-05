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
function scroll(){
    (window).scroll(function() {
        if ($(this).scrollTop() >= 80) {        
            $('#return-to-top').fadeIn(200);    
        } else {
            $('#return-to-top').fadeOut(200);   
        }
    });
    ('#return-to-top').click(function() {      
        ('body,html').animate({
            scrollTop : 0                       
        }, 500);
    });
}
