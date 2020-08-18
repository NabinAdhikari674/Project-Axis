$(document).ready(function(){
    $(document).on('click','.postFeedReactUp',function(){
        var ID = $(this).attr('id');
        var postId = ID.substring(ID.lastIndexOf("-") + 1, ID.length);
        $.ajax({
            type:'POST',
            url: getURLS("reactionURL"),
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
            url:getURLS("reactionURL"),
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

function updateReactions()
{
  $.ajax({
      type:'POST',
      url:getURLS("reactionURL"),
      data: {activity:'updateReactions'},
      success:function(response){
        if(response){
          var data = JSON.parse(response);
          $.each(data.reactionList, function( index, value )
          {
            if(value==0)
            {
              $('#postFeedReactUp-'+data.postList[index]).val(0);
              $('#popuMsg-'+data.postList[index]).html("~ React to this Post &#8628;");
            }
            if(value==1)
            {
              $('#postFeedReactUp-'+data.postList[index]).val(1);
              $('#popuMsg-'+data.postList[index]).html("+You Upped !!");
              $('#postFeedReactUp-'+data.postList[index]).css("color","blue");
            }
            if(value==2)
            {
              //alert('#post-feed-reactUp'+data.postList[index]);
              $('#postFeedReactDown-'+data.postList[index]).val(1);
              $('#popuMsg-'+data.postList[index]).html("-You Meh-ed !!");
              $('#postFeedReactDown-'+data.postList[index]).css("color","#e8807d");
            }

          });
        }
        else {
          console.log(" Update Reaction Request to updateReactions.php ERROR");
        }
          //$("#load-more"+ID+8).detach().appendTo("#post-feed");
      }
   });
   //$('load-more').parentNode.removeChild('load-more');
};

function updatePostReaction()
{

}

function updatePopPanel(postId,status,aStatus,flow)
{
  var counter = parseInt($("#popuCounter-"+postId).html());

  if(flow=='up')
  {if(status==0)
    {if(aStatus=='off')
      {
        counter+=1;
        $("#popuCounter-"+postId).html(counter);
        $("#popuMsg-"+postId).html("+You Upped !!");
      }
     else if (aStatus=='on')
      {
        counter+=2;
        $("#popuCounter-"+postId).html(counter);
        $("#popuMsg-"+postId).html("+You Upped !!");
      }
    }
   else if (status==1)
    {if (aStatus=='off')
      counter-=1;
      $("#popuCounter-"+postId).html(counter);
      $("#popuMsg-"+postId).html("~ You Retracted Up !");
     }
  }

  else if(flow=='down')
  {if(status==0)
    {if(aStatus=='off')
      {
        counter-=1;
        $("#popuCounter-"+postId).html(counter);
        $("#popuMsg-"+postId).html("-You Meh-ed !!");
      }
     else if (aStatus=='on')
      {
        counter-=2;
        $("#popuCounter-"+postId).html(counter);
        $("#popuMsg-"+postId).html("-You Meh-ed !!");
      }
    }
   else if (status==1)
    {if (aStatus=='off')
      counter+=1;
      $("#popuCounter-"+postId).html(counter);
     }
  }

}


var csrftoken = getCookie('csrftoken');
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
  }
});