$(function(){
  $('.book-card').on('click', function(){
    if( ! $(this).hasClass("noprice") ){
      $(this).siblings('.bookprice-area').slideDown();
    }
  });
  $('.noprice').on('click', function(){
    $(this).addClass('animated shake');
    toastr.error('There will be offers soon!', 'Sorry');
    toastr.options.closeButton = true;
  }).on('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
    $(this).removeClass('animated shake');
  });

})