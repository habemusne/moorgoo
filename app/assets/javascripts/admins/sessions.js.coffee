$(document).ready ->
  $.validator.addMethod "regex", ((value, element, regexp) ->
    unless regexp.constructor is RegExp
      regexp = new RegExp(regexp)
    else regexp.lastIndex = 0  if regexp.global
    @optional(element) or regexp.test(value)
  ), "Please check your input"
  $("#signinForm").validate
    rules:
      user_email: 
        required: true
        pattern: /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.[Ee][Dd][Uu]$/
    messages:
      user_email:
        required: "Please enter an email"
        pattern: "Please enter a valid email"
    errorLabelContainer: '.input_error_notice'
  return
