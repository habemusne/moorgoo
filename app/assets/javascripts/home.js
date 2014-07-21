$(function(){

  //Book Search Bar Placeholder Change
  $('.search-book-title').on('click', function(){
    $('.index-book-search').attr("placeholder", "Search By Bookname");
    $('#bookSearchType').attr("value", "title");
  });
  $('.search-book-isbn').on('click', function(){
    $('.index-book-search').attr("placeholder", "Search By ISBN");
    $('#bookSearchType').attr("value", "isbn");
  });
  $('.search-book-class').on('click', function(){
    $('.index-book-search').attr("placeholder", "Search By Class");
    $('#bookSearchType').attr("value", "course");
  });


  //"Sell" Tag Animations
  $('.arrow_container').mouseover(function(event) {
    $(this)
      .animate(
        { 
          top: 20
        }, 
        {
          duration: 40,
          easing: 'easeOutBack'
        }
      );
  });  
  $('.arrow_container').mouseout(function(event) {
    $(this)
      .animate(
        { 
          top: 0
        }, 
        {
          duration: 20,
          easing: 'easeInBounce'
        });
  });


  //Dropdown Menu Animation
  $('.my_dropdown_trigger').mouseover(function(event) {
    $('.my_dropdown_menu')[0].style.display = 'block';
  });
  $('.my_dropdown_trigger').mouseout(function(event) {
    $('.my_dropdown_menu')[0].style.display = 'none';
  });
})

