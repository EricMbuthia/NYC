$(function() {    
     
    $("#register_btn").click(function(e) {  
      e.preventDefault();
      new_speaker_data = $('#track_registration_form').serialize();
      $.ajax({
          type:"POST",
          url:"/app/our_tracks_post/",
          data: new_speaker_data,
          beforeSend: function() {
             //$('#messacge').html("<h2>Registration Form Submitted!</h2>")
          },
          cache: false,
          dataType: "json",
          success: function(data){
		  alert("Success");
            //$(".error").css({ 'display': "none" });
            if(!data['form_saved']){
			alert(data['errors']);
             /* $.each(data.errors, function(index, value){
                  $('#error_id_'+index).css({ 'display': "block" }).html(value);
              });*/
            }

            if(data.status === "ok"){
              //window.location('/accounts/activate/');
              location.href = "/app/";
            }

          }
      }); 

      return false;
    });        
});
    
   