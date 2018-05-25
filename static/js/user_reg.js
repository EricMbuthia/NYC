$(function() {    
         Stripe.setPublishableKey('pk_test_vyrZcfjLWZioZ3bOrrCe4rcj');
       function addInputNames() {
                    // Not ideal, but jQuery's validate plugin requires fields to have names
                    // so we add them at the last possible minute, in case any javascript 
                    // exceptions have caused other parts of the script to fail.
                    $(".card-number").attr("name", "card-number");
                    $(".card-cvc").attr("name", "card-cvc");
                    $(".card-expiry-year").attr("name", "card-expiry-year");
                }
         function removeInputNames() {
                    $(".card-number").removeAttr("name");
                    $(".card-cvc").removeAttr("name");
                    $(".card-expiry-year").removeAttr("name");
                }
			function makeToken(){
			
			
			
			}
    $("#regButton").click(function(e) {  
removeInputNames(); 

stripe.createToken('card', {
						number: $('.card-number').val(),
                        cvc: $('.card-cvc').val(),
                        exp_month: $('.card-expiry-month').val(), 
                        exp_year: $('.card-expiry-year').val()
}).then(function(result) {
console.log(result.token);
	form.append(result.token)
  // Handle result.error or result.token
});

      e.preventDefault();
      new_user_data = $('#user_registration_form').serialize();
      $.ajax({
          type:"POST",
          url:"/regApp/register/",
          data: new_user_data,
          beforeSend: function() {

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
    
   