$(function(){
  var USERNAME_LENGTH_ERROR_TEXT = 'Username should contain at least 6 characters';
  var EMAIL_FORMAT_ERROR_TEXT = 'Please enter a valid campus email';
  var PASSWORD_LENGTH_ERROR_TEXT = 'Password should contain at least 6 characters';
  var CONFIRM_MATCH_ERROR_TEXT = 'Passwords do not match';
  var INPUT_ERROR_NOTICE_ID = 'input_error_notice';
  var VALID_EMAIL_PATTERN = new RegExp(/^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.[Ee][Dd][Uu]$/);

  // $("#signup_confirmButton").click(false);

  $("#signup_username").keyup(function(){
    username_input = $("#signup_username")[0].value;
    email_input = $("#signup_email")[0].value;
    password_input = $("#signup_password")[0].value;
    confirm_input = $("#signup_confirm_password")[0].value;
    if (checkUsernameLength(username_input, 6) === false){
      displayError(INPUT_ERROR_NOTICE_ID, USERNAME_LENGTH_ERROR_TEXT);
    }
    else if(email_input.length > 0 && 
             checkEmailFormat(email_input, VALID_EMAIL_PATTERN) === false) {
      displayError(INPUT_ERROR_NOTICE_ID, EMAIL_FORMAT_ERROR_TEXT);
    }
    else if (password_input.length > 0 && 
              checkPasswordLength(password_input, 6) === false){
      displayError(INPUT_ERROR_NOTICE_ID, PASSWORD_LENGTH_ERROR_TEXT);
    }
    else if(confirm_input.length > 0 && 
            checkConfirmPassword(password_input, confirm_input) === false){
      displayError(INPUT_ERROR_NOTICE_ID, CONFIRM_MATCH_ERROR_TEXT);
    }
    else{
      clearError(INPUT_ERROR_NOTICE_ID);
      if (inputContainsError(INPUT_ERROR_NOTICE_ID, 
                             username_input, 
                             email_input, 
                             password_input, 
                             confirm_input) === false){
        $("#signup_confirmButton").click(true);
      }
    }
  });
  $("#signup_email").keyup(function(){
    username_input = $("#signup_username")[0].value;
    email_input = $("#signup_email")[0].value;
    password_input = $("#signup_password")[0].value;
    confirm_input = $("#signup_confirm_password")[0].value;
    if(checkEmailFormat(email_input, VALID_EMAIL_PATTERN) === false) {
      displayError(INPUT_ERROR_NOTICE_ID, EMAIL_FORMAT_ERROR_TEXT);
    }
    else if (username_input.length > 0 && 
             checkUsernameLength(username_input, 6) === false){
      displayError(INPUT_ERROR_NOTICE_ID, USERNAME_LENGTH_ERROR_TEXT);
    }
    else if (password_input.length > 0 && 
              checkPasswordLength(password_input, 6) === false){
      displayError(INPUT_ERROR_NOTICE_ID, PASSWORD_LENGTH_ERROR_TEXT);
    }
    else if(confirm_input.length > 0 && 
            checkConfirmPassword(password_input, confirm_input) === false){
      displayError(INPUT_ERROR_NOTICE_ID, CONFIRM_MATCH_ERROR_TEXT);
    }
    else{
      clearError(INPUT_ERROR_NOTICE_ID);
      if (inputContainsError(INPUT_ERROR_NOTICE_ID, 
                             username_input, 
                             email_input, 
                             password_input, 
                             confirm_input) === false){
        $("#signup_confirmButton").click(true);
      }
    }
  });
  $("#signup_password").keyup(function(){
    username_input = $("#signup_username")[0].value;
    email_input = $("#signup_email")[0].value;
    password_input = $("#signup_password")[0].value;
    confirm_input = $("#signup_confirm_password")[0].value;
    if (checkPasswordLength(password_input, 6) === false){
      displayError(INPUT_ERROR_NOTICE_ID, PASSWORD_LENGTH_ERROR_TEXT);
    }
    else if (username_input.length > 0 && 
             checkUsernameLength(username_input, 6) === false){
      displayError(INPUT_ERROR_NOTICE_ID, USERNAME_LENGTH_ERROR_TEXT);
    }
    else if(email_input.length > 0 && 
             checkEmailFormat(email_input, VALID_EMAIL_PATTERN) === false) {
      displayError(INPUT_ERROR_NOTICE_ID, EMAIL_FORMAT_ERROR_TEXT);
    }
    else if(confirm_input.length > 0 && 
            checkConfirmPassword(password_input, confirm_input) === false){
      displayError(INPUT_ERROR_NOTICE_ID, CONFIRM_MATCH_ERROR_TEXT);
    }
    else{
      clearError(INPUT_ERROR_NOTICE_ID);
      if (inputContainsError(INPUT_ERROR_NOTICE_ID, 
                             username_input, 
                             email_input, 
                             password_input, 
                             confirm_input) === false){
        $("#signup_confirmButton").click(true);
      }
    }
  });
  $("#signup_confirm_password").keyup(function(){
    username_input = $("#signup_username")[0].value;
    email_input = $("#signup_email")[0].value;
    password_input = $("#signup_password")[0].value;
    confirm_input = $("#signup_confirm_password")[0].value;
    if(checkConfirmPassword(password_input, confirm_input) === false){
      displayError(INPUT_ERROR_NOTICE_ID, CONFIRM_MATCH_ERROR_TEXT);
    }
    else if (username_input.length > 0 &&
             checkUsernameLength(username_input, 6) === false){
      displayError(INPUT_ERROR_NOTICE_ID, USERNAME_LENGTH_ERROR_TEXT);
    }
    else if(email_input.length > 0 && 
             checkEmailFormat(email_input, VALID_EMAIL_PATTERN) === false) {
      displayError(INPUT_ERROR_NOTICE_ID, EMAIL_FORMAT_ERROR_TEXT);
    }
    else if (password_input.length > 0 && 
             checkPasswordLength(password_input, 6) === false){
      displayError(INPUT_ERROR_NOTICE_ID, PASSWORD_LENGTH_ERROR_TEXT);
    }
    else{
      clearError(INPUT_ERROR_NOTICE_ID);
      if (inputContainsError(INPUT_ERROR_NOTICE_ID, 
                             username_input, 
                             email_input, 
                             password_input, 
                             confirm_input) === false){
        $("#signup_confirmButton").click(true);
      }
    }
  });
});

function displayError(errorTagId, errorContent){
  document.getElementById(errorTagId).innerHTML = errorContent;
}

function clearError(errorTagId){
  document.getElementById(errorTagId).innerHTML = '';
}

function checkUsernameLength(username, validLength){
    if (username.length < validLength){
      return false;
    }else{
      return true;
    }
}

function checkEmailFormat(email, valid_regex){
    if (valid_regex.test(email) === false){
      return false;
    }else{
      return true;    
    }
}

function checkPasswordLength(password, validLength){
  if (password.length < validLength)
    return false;
  else
    return true;
}

function checkConfirmPassword(password, confirm){
  if (password !== confirm)
    return false;
  else
    return true;
}

function inputContainsError(errorTagId, username, email, password, confirm_password){
  if (document.getElementById(errorTagId).innerHTML === '' &&
      username.length > 0 &&
      email.length > 0 &&
      password.length > 0 &&
      confirm_password.length > 0){
    return false;
  }else {
    return true;
  }
}
