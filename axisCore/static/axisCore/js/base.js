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

    $(document).on('click','.uploadPostButton',function(){
      document.getElementById('overlapContentPage').style.display='block';
      document.getElementById('axisMenu').style.display='none';
      document.body.style.overflow = "hidden";
      document.getElementById("axisNavbar").style.top = "0";
      console.log("Button Pressed : Upload Post");
      //alert("Button Pressed");
      var csrf_token = getCookie('csrftoken');
        $.ajax({
            type:'POST',
            url:'base/postForm/',
            data: {"csrfmiddlewaretoken" : csrf_token},
            success:function(response){
              console.log("Form Received");
              //$(response).hide().appendTo(".overlapContentPage").fadeIn(10);
              if ($('.uploadPostForm').length) {
                 document.getElementById('uploadPostForm').style.display='block';
               }
               else{
                 $(".overlapContentPage").append(response);
               }
            }
        });
     });
    $(document).on('click','.uploadPostFormCloseButton',function(){
       document.getElementById('overlapContentPage').style.display='none';
       document.getElementById('uploadPostForm').style.display='none';
       document.getElementById('axisMenu').style.display='block';
       document.body.style.overflow = "scroll";
      });

    $(document).on('click','.newPostSubmitButton',function(){
        console.log("Button Pressed : Submit Post");
        var csrf_token = getCookie('csrftoken');
          $.ajax({
              type:'POST',
              url:'base/uploadPost/',
              data: {"csrfmiddlewaretoken" : csrf_token,uploadPostForm:$('#postForm').val() },
              success:function(response){
                console.log("Received");
                //$(response).hide().appendTo(".overlapContentPage").fadeIn(10);
                if ($('.uploadPostForm').length) {
                   //document.getElementById('uploadPostForm').style.display='block';
                 }
                 else{
                   //$(".overlapContentPage").append(response);
                 }
              }
          });
       });



});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function uploadPost(formData){
    console.log("Uploading your Post")
}
