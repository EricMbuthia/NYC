$(function() {    
     
    $("#addEmail").click(function(e) {  
      e.preventDefault();
      new_email_data = $('#email_add').serialize();
      $.ajax({
          type:"POST",
          url:"/passenger/addPaypal/",
          data: new_email_data,
          beforeSend: function() {
             //$('#messacge').html("<h2>Registration Form Submitted!</h2>")
          },
          cache: false,
          dataType: "json",
          success: function(data){
		  alert("Success");
            //$(".error").css({ 'display': "none" });
          //  if(!data['form_saved']){
			/*alert(data['errors']);
             /* $.each(data.errors, function(index, value){
                  $('#error_id_'+index).css({ 'display': "block" }).html(value);
              })
            }*/

            if(data.status === "ok"){
              //window.location('/accounts/activate/');
              //location.href = "/passenger/";
            alert("very okay");
			}
			else if(data.status === "not_ok"){
			alert("not okay")
			//location.href="/passenger/error/";
			}

          },
		  failure: function(data){
		    alert("Failure");
		  }
      }); 

      return false;
    });     
//
   $("#submitTickets").click(function(e) {  
      e.preventDefault();
      new_ticket_data = $('#multiple_pass').serialize();
      $.ajax({
          type:"POST",
          url:"/passenger/buyTickets/",
          data: new_ticket_data,
          beforeSend: function() {
             //$('#messacge').html("<h2>Registration Form Submitted!</h2>")
          },
          cache: false,
          dataType: "json",
          success: function(data){
		  alert("Success");
            //$(".error").css({ 'display': "none" });
          //  if(!data['form_saved']){
			/*alert(data['errors']);
             /* $.each(data.errors, function(index, value){
                  $('#error_id_'+index).css({ 'display': "block" }).html(value);
              })
            }*/

            if(data.status === "ok"){
              //window.location('/accounts/activate/');
              //location.href = "/passenger/";
            alert("very okay");
			}
			else if(data.status === "not_ok"){
			alert("not okay")
			//location.href="/passenger/error/";
			}

          },
		  failure: function(data){
		    alert("Failure");
		  }
      }); 

      return false;
    });    	

 $("#register").click(function(e) {  
      e.preventDefault();
      new_registration_data = $('#registration').serialize();
      $.ajax({
          type:"POST",
          url:"/authetr/register/",
          data: new_registration_data,
          beforeSend: function() {
             //$('#messacge').html("<h2>Registration Form Submitted!</h2>")
          },
          cache: false,
          dataType: "json",
          success: function(data){
		  //alert("Success");
            //$(".error").css({ 'display': "none" });
          //  if(!data['form_saved']){
			/*alert(data['errors']);
             /* $.each(data.errors, function(index, value){
                  $('#error_id_'+index).css({ 'display': "block" }).html(value);
              })
            }*/

            if(data.status === "ok"){
              //window.location('/accounts/activate/');
              //location.href = "/passenger/";
            alert("very okay");
			}
			else if(data.status === "not_ok"){
			alert("not okay")
			//location.href="/passenger/error/";
			}

          },
		  failure: function(data){
		    alert("Failure");
		  }
      }); 

      return false;
    });    	
	 $("#activate").click(function(e) {  
      e.preventDefault();
      new_activation_data = $('#confirmForm').serialize();
      $.ajax({
          type:"POST",
          url:"/authetr/verify/",
          data: new_activation_data,
          beforeSend: function() {
             //$('#messacge').html("<h2>Registration Form Submitted!</h2>")
          },
          cache: false,
          dataType: "json",
          success: function(data){
		  //alert("Success");
            //$(".error").css({ 'display': "none" });
          //  if(!data['form_saved']){
			/*alert(data['errors']);
             /* $.each(data.errors, function(index, value){
                  $('#error_id_'+index).css({ 'display': "block" }).html(value);
              })
            }*/

            if(data.status === "ok"){
              //window.location('/accounts/activate/');
              //location.href = "/passenger/";
            alert("verify okay");
			}
			else if(data.status === "not_ok"){
			alert("verify not okay")
			//location.href="/passenger/error/";
			}

          },
		  failure: function(data){
		    alert("Failure");
		  }
      }); 

      return false;
    }); 
	$("#submitLogin").click(function(e) {  
      e.preventDefault();
      new_login_data = $('#loginForm').serialize();
      $.ajax({
          type:"POST",
          url:"/authetr/login/",
          data: new_login_data,
          beforeSend: function() {
             //$('#messacge').html("<h2>Registration Form Submitted!</h2>")
          },
          cache: false,
          dataType: "json",
          success: function(data){
		  //alert("Success");
            //$(".error").css({ 'display': "none" });
          //  if(!data['form_saved']){
			/*alert(data['errors']);
             /* $.each(data.errors, function(index, value){
                  $('#error_id_'+index).css({ 'display': "block" }).html(value);
              })
            }*/

            if(data.status === "ok"){
              //window.location('/accounts/activate/');
              //location.href = "/passenger/";
            alert("very okay");
			}
			else if(data.status === "not_ok"){
			alert("not okay")
			//location.href="/passenger/error/";
			}

          },
		  failure: function(data){
		    alert("Failure");
		  }
      }); 

      return false;
    });    	
});
    
   