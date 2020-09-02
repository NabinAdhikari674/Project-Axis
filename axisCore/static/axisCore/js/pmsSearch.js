
$(document).ready(function(){
    $(document).on ('click','searchQueryField',function () {
       
  });
  
    

    $(document).on('click','.searchQueryButton',function(){
        //console.log("Button Pressed : Submit Post");
        var fd = new FormData();
      fd.append('category1', $('#category1').val());
      fd.append('choosePost', $('#choosePost').val());
      fd.append('status', $('#status').val());
        console.log("clicked")

        
  
          $.ajax({
              type:'GET',
              url:getBaseURLs('pmssearchhURL'),
              data: {fd},
              processData: false,
              contentType: false,
              success:function(response){
                    $(".axisNavbar").append(response);

                
               },
              error: function(response) {
                alert("Something Went Wrong. Try Again !!")
              }
          });
       });
  
  });
  
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
  