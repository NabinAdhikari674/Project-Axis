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

    
    $(document).on('click','.uploadPostFormCloseButton',function(){
       document.getElementById('overlapContentPage').style.display='none';
       document.body.style.overflow = "scroll";
       document.getElementById('axisMenu').style.display='block';
       try{
           document.getElementById('uploadPostForm').remove();
           document.getElementById('infoDiv').remove();
        }
       catch(err){};
       try{$('.postDetailView').remove();}
       catch(err){};    
      });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});