$(document).ready(function(){
    $(document).on('click','.postFeedNoReact',function(){
      alert("You have to be Logged In To be able to React On Posts !!");
    });
    $(document).on('click','.postFeedReactUp',function(){
        var ID = $(this).attr('id');
        var postId = ID.substring(ID.lastIndexOf("-") + 1, ID.length);
        $.ajax({
            type:'POST',
            url: getPostURLS("reactionURL"),
            data: {postId:postId,reaction:1},
            success:function(response){
              if(response.Reaction=='Upped')
              {
                $('#'+ID).css("color", "blue");
                $('#postFeedReactDown-'+postId).css("color", "grey");
                $("#popuCounter-"+postId).html(response.Counter);
                $("#popuMsg-"+postId).html("+You Upped !!");

              }
              else if (response.Reaction=='Updated')
              {
                $('#'+ID).css("color", "grey");
                $("#popuCounter-"+postId).html(response.Counter);
                $("#popuMsg-"+postId).html("~ You Retracted Up !");
              }
              else
              { console.log(response); }
            }
        });
    });

    $(document).on('click','.postFeedReactDown',function(){
        var ID = $(this).attr('id');
        var postId = ID.substring(ID.lastIndexOf("-") + 1, ID.length);
        $.ajax({
            type:'POST',
            url:getPostURLS("reactionURL"),
            data: {postId:postId,reaction:2},
            success:function(response){
              if(response.Reaction=='Down')
              {
                $('#'+ID).css("color", "#e8807d");
                $('#postFeedReactUp-'+postId).css("color", "grey");
                $("#popuCounter-"+postId).html(response.Counter);
                $("#popuMsg-"+postId).html("-You Meh-ed !!");
              }
              else if (response.Reaction=='Updated')
              {
                $('#'+ID).css("color", "grey");
                $("#popuCounter-"+postId).html(response.Counter);
                $("#popuMsg-"+postId).html("~ You Retracted Meh !");
              }
              else
              { console.log(response); }
            }
        });
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