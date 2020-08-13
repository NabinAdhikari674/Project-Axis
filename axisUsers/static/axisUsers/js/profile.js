$(document).ready(function(){  
    profileUsername = $('#profileUsername').val();
    profileEmail = $('#profileEmail').val();
    profileNumber = $('#profileNumber').val();
    profileFirstName = $('#profileFirstName').val();
    profileLastName = $('#profileLastName').val();
    profileGender = $('#profileGender').val();
    profileCountry = $('#profileCountry').val();
    profileState = $('#profileState').val();
    profileCity = $('#profileCity').val();
    profileArea = $('#profileArea').val();
    


    $(document).on('click','#profileEditButton',function(){
        document.getElementById('profileConfirmDiv').style.display='block';

        setAttributeToInputReadOnly(false);
       
      });
    $(document).on('click','#profileCancelButton',function(){
        document.getElementById('profileConfirmDiv').style.display='none';

        setAttributeToInputReadOnly(true);
        $(".profileErrors").html("");
        $("#profileUsername").val(profileUsername);
        $("#profileEmail").val(profileEmail);
        $("#profileNumber").val(profileNumber);
        $("#profileFirstName").val(profileFirstName);
        $("#profileLastName").val(profileLastName);
        $("#profileGender").val(profileGender);
        $("#profileCountry").val(profileCountry);
        $("#profileState").val(profileState);
        $("#profileCity").val(profileCity);
        $("#profileArea").val(profileArea);

    });

    $(document).on('click','#profileUserAccEditButton',function(){
        document.getElementById('profileUserAccConfirmDiv').style.display='block';

        document.getElementById("profileUsername").readOnly = false;
        document.getElementById("profileEmail").readOnly = false;
        document.getElementById("profileNumber").readOnly = false;

        
      });
    $(document).on('click','#profileUserAccCancelButton',function(){
        document.getElementById('profileUserAccConfirmDiv').style.display='none';

        document.getElementById("profileUsername").readOnly = true;
        $("#profileUsername").val(profileUsername);
        document.getElementById("profileEmail").readOnly = true;
        $("#profileEmail").val(profileEmail);
        document.getElementById("profileNumber").readOnly = true;
        $("#profileNumber").val(profileNumber);

    });

    $(document).on('click','#profileUserInfoEditButton',function(){
        document.getElementById('profileUserInfoConfirmDiv').style.display='block';

        document.getElementById("profileFirstName").readOnly = false;
        document.getElementById("profileLastName").readOnly = false;
        document.getElementById("profileGender").readOnly = false;
        document.getElementById("profileCountry").readOnly = false;
        document.getElementById("profileState").readOnly = false;
        document.getElementById("profileCity").readOnly = false;
        document.getElementById("profileArea").readOnly = false;
      });
    $(document).on('click','#profileUserInfoCancelButton',function(){
        document.getElementById('profileUserInfoConfirmDiv').style.display='none';

        document.getElementById("profileFirstName").readOnly = true;
        $("#profileFirstName").val(profileFirstName);
        document.getElementById("profileLastName").readOnly = true;
        $("#profileLastName").val(profileLastName);
        document.getElementById("profileGender").readOnly = true;
        $("#profileGender").val(profileGender);
        document.getElementById("profileCountry").readOnly = true;
        $("#profileCountry").val(profileCountry);
        document.getElementById("profileState").readOnly = true;
        $("#profileState").val(profileState);
        document.getElementById("profileCity").readOnly = true;
        $("#profileCity").val(profileCity);
        document.getElementById("profileArea").readOnly = true;
        $("#profileArea").val(profileArea);
    });
});

function setAttributeToInputReadOnly(x){
    document.getElementById("profileUsername").readOnly = x;
    document.getElementById("profileEmail").readOnly = x;
    document.getElementById("profileNumber").readOnly = x;
    document.getElementById("profileFirstName").readOnly = x;
    document.getElementById("profileLastName").readOnly = x;
    document.getElementById("profileGender").readOnly = x;
    document.getElementById("profileCountry").readOnly = x;
    document.getElementById("profileState").readOnly = x;
    document.getElementById("profileCity").readOnly = x;
    document.getElementById("profileArea").readOnly = x;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});