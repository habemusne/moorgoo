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
  $('.arrow-container').mouseover(function(event) {
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
  $('.arrow-container').mouseout(function(event) {
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
  $('.my-dropdown-trigger').mouseover(function(event) {
    $('.my-dropdown-menu')[0].style.display = 'block';
  });
  $('.my-dropdown-trigger').mouseout(function(event) {
    $('.my-dropdown-menu')[0].style.display = 'none';
  });
})

