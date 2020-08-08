
$(document).ready(function(){
    $(document).on('click','.searchQueryButton',function(){
        //console.log("Button Pressed : Submit Post");
        document.getElementById('overlapContentPage').style.display='block';
        document.getElementById('axisMenu').style.display='none';
        document.body.style.overflow = "hidden";
        document.getElementById("axisNavbar").style.top = "0";
        var fd =  $('#inputSuccess4').val();
        //console.log("clicked")
          $.ajax({
              type:'GET',
              url:'search/',
              data: fd,
              processData: false,
              contentType: false,
              success:function(response){
                    $(".overlapContentPage").append(response);

                
               },
              error: function(response) {
                alert("Something Went Wrong. Try Again !!")
              }
          });
       });
  
  });
function searchClicker(){
    $('.searchQueryButton').click();
};

  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
  
