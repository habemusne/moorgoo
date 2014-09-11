$(function(){
  $('.role-master').click(function() {
    $('.role-marketing-container')[0].style.display = "none";
    $('.role-technical-container')[0].style.display = "none";
    $('.role-master-container').fadeIn();
  });
  $('.role-marketing').click(function() {
    $('.role-master-container')[0].style.display = "none";
    $('.role-technical-container')[0].style.display = "none";
    $('.role-marketing-container').fadeIn();
  });
  $('.role-technical').click(function() {
    $('.role-master-container')[0].style.display = "none";
    $('.role-marketing-container')[0].style.display = "none";
    $('.role-technical-container').fadeIn();
  });
});