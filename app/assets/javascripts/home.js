function isEmailValidate() {
  var x = document.forms["myform"]["email"].value;
  var filter=/^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
  if (filter.test(x)){
    testresults=true;
  }
  else {
    testresults=false;
  }
  return (testresults);
}
function validateEmail(){
  if(isEmailValidate()){
    $("#submitemail").attr("disabled", false);
    $("#email").css("border-color","#12c3cc");
    $("#emaildiv").removeClass("hint--top hint--always");
    $("#emaildiv").removeAttr('data-hint', "");
  }
  else{
    $("#submitemail").attr("disabled", true);
    $("#email").css("border-color","#e86343");
    $("#emaildiv").addClass("hint--top hint--always");
    $("#emaildiv").attr('data-hint', "请输入格式正确的Email地址");
  }
}
// $(document).ready(function(){
// });
$(function(){
  $("#submitemail").attr("disabled", true);
  $("#email").css("border-color","#e86343");
});
