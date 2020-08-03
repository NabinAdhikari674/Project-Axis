$(document).ready(function(){
  $(document).on('click','.advancedPostButton',function(){
    if (document.getElementById('advancedPostTab').style.display=='none')
    {
      document.getElementById('advancedPostTab').style.display='block';
    }
    else{
      document.getElementById('advancedPostTab').style.display='none';
    }

  });

  $(document).on('click','.newPostSubmitButton',function(){
      //console.log("Button Pressed : Submit Post");
      var fd = new FormData();
      fd.append('postTitle', $('#newPostTitle').val());
      fd.append('category', $('#category').val());
      fd.append('postLevel', $('#postLevel').val());
      fd.append('axisStatus', $('#axisStatus').val());
      fd.append('budget', $('#budget').val());
      fd.append('startDate', $('#startDate').val());
      fd.append('endDate', $('#endDate').val());
      fd.append('content', $('#newPostContent').val());

        $.ajax({
            type:'POST',
            url:'base/uploadPost/',
            data: fd,
            processData: false,
            contentType: false,
            success:function(response){
              if (response.Form=='SAVED'){
                 alert("Your Post Was Sucessfully Uploaded !!");
                 document.getElementById('uploadPostForm').style.display='none';
                 document.getElementById('overlapContentPage').style.display='none';
                 document.getElementById('axisMenu').style.display='block';
                 document.body.style.overflow = "scroll";
                  }
             },
            error: function(data) {
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
