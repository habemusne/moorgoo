$(document).ready ->
  $.validator.addMethod "regex", ((value, element, regexp) ->
    unless regexp.constructor is RegExp
      regexp = new RegExp(regexp)
    else regexp.lastIndex = 0  if regexp.global
    @optional(element) or regexp.test(value)
  ), "Please check your input"
  $("#isbnForm").validate
    rules:
      search:
        required: true
        pattern: /^(97(8|9))?\d{9}(\d|X)$/
    messages:
      search:
        required: "Please enter an ISBN"
        pattern: "Please enter a valid ISBN"
    errorClass: 'input_error_notice'
    errorLabelContainer: '.input_error_notice'
    $("#tabid1 a").click (e) ->
      e.preventDefault()
      $(this).tab "show"
    $("#tabid2 a").click (e) ->
      e.preventDefault()
      $(this).tab "show"
    $('#tabid1 a[href="#tabid1"]').tab('show')
    $('#tabid2 a[href="#tabid2"]').tab('show')