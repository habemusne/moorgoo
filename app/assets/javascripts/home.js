$(function(){
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
})