$(document).ready( function() {
	
	$( "#mybutton" ).button();
	$( "#radioset" ).buttonset();
	$( "#country" ).selectmenu();
	$( "#datepicker" ).datepicker({
		inline: true
	});	
		

	// validate the comment form when it is submitted
	

	// validate signup form on keyup and submit
	$("#forms1").validate({
		rules: {
			firstname: "required",
			lastname: "required",
			username: {
				required: true,
				minlength: 2
			},
			password: {
				required: true,
				minlength: 5
			},
			confirm: {
				required: true,
				minlength: 5,
				equalTo: "#password"
			},
			email: {
				required: true,
				email: true
			},
			agree: "required"
		},
		messages: {
			firstname: "Please enter your firstname",
			lastname: "Please enter your lastname",
			username: {
				required: "Please enter a username",
				minlength: "Your username must consist of at least 2 characters"
			},
			password: {
				required: "Please provide a password",
				minlength: "Your password must be at least 5 characters long"
			},
			confirm_password: {
				required: "Please provide a password",
				minlength: "Your password must be at least 5 characters long",
				equalTo: "Please enter the same password as above"
			},
			email: "Please enter a valid email address",
			agree: "Please accept our policy"
		}, 
		errorLabelContainer: "#error"
	});
	
	$( ".error" ).live().addClass( "ui-state-error" ); //modify!!!
	
	
		


	
});
