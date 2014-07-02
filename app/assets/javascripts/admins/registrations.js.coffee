$(document).ready ->
  $.validator.addMethod "regex", ((value, element, regexp) ->
    unless regexp.constructor is RegExp
      regexp = new RegExp(regexp)
    else regexp.lastIndex = 0  if regexp.global
    @optional(element) or regexp.test(value)
  ), "Please check your input"
  $("#signupForm").validate
    rules:
      user_name:
      	required: true
      	minlength: 6
      user_email: 
        required: true
        pattern: /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.[Ee][Dd][Uu]$/
      user_password:
        required: true
        minlength: 6
      user_password_confirmation:
        required: true
        equalTo: '#user_password'
    messages:
      user_name:
        required: "Please enter a username"
        minlength: "Username should be at least 6 characters"
      user_email:
        required: "Please enter an email"
        pattern: "Please enter a '.edu' email"
      user_password:
        required: "Please enter a password"
        minlength: "Password should be at least 6 characters"
      user_password_confirmation:
        required: "Please repeat your password"
        equalTo: "Passwords do not match"
    errorLabelContainer: '#error'
  return
