$(function(){
  $('#econ41button').on('click', function(){
    $('li').removeClass('active-li');
    $(this).parent().addClass('active-li');
    document.getElementById('youtube-video').innerHTML = '<iframe width="640" height="360" src="//www.youtube.com/embed/OleHnPjQHrE" frameborder="0" allowfullscreen></iframe>'
    $('.video-intro-container').show()
    // var inst = ABP.create( document.getElementById('load-player'), {
    //   'src': 'http://static.cdn.moe/ccltestingvideos/otsukimi_recital.mp4',
    //   'width': 600,
    //   'height': 400
    // });
    // CommentLoader('assets/otsukimi.xml', inst.cmManager);
    
  });
});


