

 $(document).ready(function(){
  alert("my.jssss");
  fetch_data();
  setInterval( function () {
reseter(); // user paging is not reset on reload
}, 5000 );
  function fetch_data()
  {
   var dataTable = $('#user_data').DataTable({

    //"processing" : true,
    //"serverSide" : true,
	//"paging": false,
    //"order" : [],
	"bServerSide": true,
         
         "bProcessing": true,
    "ajax" : {
	      //  headers: { "X-CSRFToken": getCookie("csrftoken") },
   
			
	/*"columns":[
	{"data":"title"},
	{"data":"abstract"},
	{"data":"track"},
	{"data":"speaker"},
	{"data":"status"},
	//https://stackoverflow.com/questions/25975086/django-datatables-load-ajax-data-load
	],*/

     //url:"http://127.0.0.1:8000/dynamic_ajax_viewer/",
     //type:"POST"
    },
	"sAjaxSource": data("http://127.0.0.1:8000/dynamic_ajax_viewer/")
   });
  }
  function reseter(){
     $('#user_data').DataTable().destroy();
     fetch_data();
  }
  function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }
  function update_data(id, column_name, value)
  {
   $.ajax({
    url:"update_entre.php",
    method:"POST",
    data:{id:id, column_name:column_name, value:value},
    success:function(data)
    {
     $jq('#alert_message').html('<div class="alert alert-success">'+data+'</div>');  
    }
   });
   setInterval(function(){
    $('#alert_message').html('');
   }, 1235000);
  }
  

  $(document).on('blur', '.update', function(){
   var id = $(this).data("id");
   var column_name = $(this).data("column");
   var value = $(this).text();
   update_data(id, column_name, value);
  });
  $('#entre_vote').click(function(){
 var id=  $('input[name=entre]:checked').val(); 
 var column_name= "last_name";
 //var calc= data["last"]
 var value ="6"
    update_data(id, column_name, value);
  });
  $('#add').click(function(){
   var html = '<tr>';
   html += '<td contenteditable id="data1"></td>';
   html += '<td contenteditable id="data2"></td>';
   html += '<td><button type="button" name="insert" id="insert" class="btn btn-success btn-xs">Insert</button></td>';
   html += '</tr>';
   $('#user_data tbody').prepend(html);
  });
  
  $(document).on('click', '#insert', function(){
   var first_name = $('#data1').text();
   var last_name = $('#data2').text();
   if(first_name != '' && last_name != '')
   {
    $.ajax({
     url:"insert.php",
     method:"POST",
     data:{first_name:first_name, last_name:last_name},
     success:function(data)
     {
      $jq('#alert_message').html('<div class="alert alert-success">'+data+'</div>');      $('#user_data').DataTable().destroy();
      fetch_data();
     }
    });
    setInterval(function(){
     $('#alert_message').html('');
    }, 1235000);
   }
   else
   {
    alert("Both Fields is required");
   }
  });
  
  $(document).on('click', '.delete', function(){
   var id = $(this).attr("id");
   if(confirm("Are you sure you want to remove this?"))
   {
    $.ajax({
     url:"delete.php",
     method:"POST",
     data:{id:id},
     success:function(data){
      $jq('#alert_message').html('<div class="alert alert-success">'+data+'</div>');      $('#user_data').DataTable().destroy();
      fetch_data();
     }
    });
    setInterval(function(){
     $('#alert_message').html('');
    }, 1235000);
   }
  });
 });
