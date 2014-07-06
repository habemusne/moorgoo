validate = undefined
validate = ->
  username = undefined
  username = document.getElementById("user_name")
  console.log username
  document.getElementById("input_error_notice").innerHTML = "Well Well Well"  if username.length < 6
  return