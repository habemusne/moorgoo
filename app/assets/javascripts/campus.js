$(".active-campus-img").click(function(event) {

  //Disable the shadow
  $(this).siblings().css("display", "none");

  //display the dialogue
  $(".category-dialogue").css("display", "block");
});


$(function() {
  $('a[href*=#]:not([href=#])').click(function() {
  	console.log("Hello");
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {

      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 500);
        return false;
      }
    }
  });
});
