$(".campus-img").click(function(event) {

  //Disable the shadow
  $(this).siblings().css("display", "none");

  //display the dialogue
  $(".category-dialogue").css("display", "block");
});

