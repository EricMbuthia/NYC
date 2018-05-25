$(function() {    
     
    $("#regButton").click(function(e) {  
      e.preventDefault();
      new_user_data = $('#user_registration_form').serialize();
      $.ajax({
          type:"POST",
          url:"/regApp/register/",
          data: new_user_data,
          beforeSend: function() {
             //fdfsd4AQ2@ $('#messacge').html("<h2>Registration Form Submitted!</h2>")
          },
          cache: false,
          dataType: "json",
          success: function(data){
		  alert("Success");
            //$(".error").css({ 'display': "none" });
            if(!data['form_saved']){
			$( "#error_display" ).addClass( "alert alert-warning alert-dismissable" );
		$('#error_display').html(data['errors']);

			//alert(data['errors']);
             /* $.each(data.errors, function(index, value){
                  $('#error_id_'+index).css({ 'display': "block" }).html(value);
              });*/
            }

            if(data.status === "ok"){
              //window.location('/accounts/activate/');
             location.href = "/";
            }

          }
      }); 

      return false;
    });  
$("#loginButton").click(function(e) {  
      e.preventDefault();
      new_user_data = $('#user_registration_form').serialize();
      $.ajax({
          type:"POST",
          url:"/regApp/registration/",
          data: new_user_data,
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
              //location.href = "/regApp/registered/";
            }

          }
      }); 

      return false;
    });	
});
    
   