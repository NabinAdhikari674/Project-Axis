$(document).ready(function(){
    var prevScrollpos = window.pageYOffset;
    window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
      if (prevScrollpos > currentScrollPos) {
        document.getElementById("axisNavbar").style.top = "0";
      } else {
        document.getElementById("axisNavbar").style.top = "-50px";
      }
      prevScrollpos = currentScrollPos;
    }
});
