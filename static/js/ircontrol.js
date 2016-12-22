function send_ir_command(action){
	var device= $('#device').val();
	
	$.ajax({
	    type: "GET",
	    url: "control?device=" + device +"&action=" + action,
	    success: function (response) {
			console.log(response);
	    },
	    error: function (request, status, err) {
	    	console.log(err);
	    }
	});
}

function render_device(action){
	var device= $('#device').val();
	$('#device-wrapper').load('render?device='+ device);
}