$(document).ready(function(){
  $(document).on('click','.advancedPostButton',function(){
    if (document.getElementById('advancedPostTab').style.display=='none'){
      document.getElementById('advancedPostTab').style.display='block';
    }
    else{
      document.getElementById('advancedPostTab').style.display='none';
    }
  });
});