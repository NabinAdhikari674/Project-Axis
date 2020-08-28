$(document).ready(function(){
    $(document).on('click','.postFeedViewButton',function(){
        var ID = $(this).attr('id');
        var postId = ID.substring(ID.lastIndexOf("-") + 1, ID.length);
        $.ajax({
            type:'GET',
            url: getPostURLS("postDetailURL"),
            data: {postId:postId},
            success:function(response){
                document.getElementById('overlapContentPage').style.display='block';
                document.getElementById('axisMenu').style.display='none';
                document.body.style.overflow = "hidden";
                document.getElementById("axisNavbar").style.top = "0";
                if ($('.postDetailView').length) {
                    try{$('.postDetailView').remove();}
                    catch(err){};
                }
                $(".overlapContentPage").append(response);
            }
        });
    });
    $(document).on('click','.detailedPostComment',function(){
        document.getElementById('newCommentPostBox').style.display='block';
    });
    $(document).on('click','.closeCommentPostButton',function(){
        document.getElementById('newCommentPostBox').style.display='none';
    });
});


var csrftoken = getCookie('csrftoken');
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
  }
});