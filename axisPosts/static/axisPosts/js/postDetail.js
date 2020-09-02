$(document).ready(function(){
    $(document).on('click','.postFeedViewButton',function(){
        let ID = $(this).attr('id');
        let postId = ID.substring(ID.lastIndexOf("-") + 1, ID.length);
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
    $(document).on('click','.commentReply',function(){
        let ID = $(this).attr('id');
        let cid = ID.substring(ID.lastIndexOf("-") + 1, ID.length);
        try{
            document.getElementById('replyCommentPostBox-'+cid).style.display='block';
            return;
        }
        catch(err){}
        ID = $(this).parents().eq(3).prop('id');
        let pid = ID.substring(ID.lastIndexOf("-") + 1, ID.length);
        let cb = document.querySelector('.newCommentPostBox').cloneNode( true );
        cb.id = "replyCommentPostBox-"+cid;
        cb.querySelector(".newCommentPostForm").id= "replycommentPostForm-"+cid;
        cb.querySelector(".newCommentPost").id= "replyCommentPost-"+cid;
        cb.querySelector(".postNewComment").id= "replyNewComment-"+cid;
        cb.querySelector(".postNewComment").classList.remove("pncP0");
        cb.querySelector(".postNewComment").classList.add("rncPx");
        cb.style.display="block";
        if ($('replyCommentPostBox-'+cid).length) {
            document.getElementById('replyCommentPostBox-'+cid).style.display='block';
          }
        else{
            $(this).parents().eq(2).append(cb);
        }
    });
    $(document).on('click','.pncP0',function(){
        let ID = $(this).attr('id');
        let pid = ID.substring(ID.lastIndexOf("-") + 1, ID.length);
        let c = $("#newCommentPost-"+pid).val();
        //if (!(document.querySelector('#newCommentPostForm-'+postId)).checkValidity()) {return;}
        if (!c){alert("Comment cannot be empty !! ");return;}
        $.ajax({
            type:'GET',
            url: getPostURLS("newCommentURL"),
            data: {pid:pid,cmt:c,cid:null},
            success:function(response){
                if(response.Comment){
                    alert(response.Comment);
                }
                try{$(response).hide().prependTo(".commentsFeed").fadeIn(900);}
                catch(err){};
                document.getElementById('newCommentPostBox').style.display='none';
            }
        });
    });

    $(document).on('click','.rncPx',function(){
        let ID = $(this).attr('id');
        let cid = ID.substring(ID.lastIndexOf("-") + 1, ID.length);
        ID = $(this).parents().eq(3).prop('id');
        let pid = ID.substring(ID.lastIndexOf("-") + 1, ID.length);
        let cbx = document.getElementById("commentBox-"+cid);
        let c = $("#replyCommentPost-"+cid).val();
        if (!c){alert("Comment cannot be empty !! ");return;}
        $.ajax({
            type:'GET',
            url: getPostURLS("newCommentURL"),
            data: {pid:pid,cmt:c,cid:cid},
            success:function(response){
                document.getElementById('replyCommentPostBox-'+cid).style.display='none';
                if(response.Comment){
                    alert(response.Comment);
                }
                try{
                    //$(response).hide().prependTo(".commentsFeed").fadeIn(900);
                    $(response).insertBefore(cbx.nextSibling).hide().fadeIn(1000);
                    //cbx.parentNode.insertBefore($(response)[0], cbx.nextSibling);
                    //$(response).hide().fadeIn(2000);
                    //parentNode.insertBefore(newNode, referenceNode)
                }
                catch(err){console.log("Comment not Appended : "+err);}; 
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