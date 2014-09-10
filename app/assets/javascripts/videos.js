$(function(){
  $('#video-intro-moorgee').tooltip();
  $('#econ41button').on('click', function(){
    $('li').removeClass('active-li');
    $(this).parent().addClass('active-li');
    document.getElementById('youtube-video').innerHTML = '<iframe width="640" height="360" src="//www.youtube.com/embed/OleHnPjQHrE" frameborder="0" allowfullscreen></iframe>'
    $('.video-intro-container').show()
    $('.course-desc').show()
    document.getElementById('below-title').innerHTML = "Econ 4 video 1 会计账户介绍";
    document.getElementById('below-desc').innerHTML = "Introduction to the principle of accounting by learning the accounts and understand how to differentiate among asset, liabilities and owners equities. What is accounting and why should we learn accounting?"
    document.getElementById('below-summ').innerHTML = "1. 什么是会计？ 什么是金融市场？ 金融市场简介<br/>2. 会计账户介绍，名称解释，例子分析<br/>3. 复式会计记账方式（Debit=借； credit=贷） 有借必有贷，借贷必相等<br/>4. Differentiate what is permanent account and what is temporary account.";
    document.getElementById('video-intro-class-name').innerHTML = "Class Name: Econ4, Principle of Accounting (Basic Introduction)";
    document.getElementById('video-intro-moorgee').innerHTML = "Moorgee: Alex (冬菇弟弟) ";
    document.getElementById('video-intro-moorgee').setAttribute("data-original-title", "如果在讲课当中大家发现冬菇弟弟有任何出错的地方，请大家毫不留情的指出来，我一定会在下面的准备中努力提高，为大家准备更有质量的辅助视频，谢谢大家。");
    //document.getElementById('video-intro-moorgee').title = "Lorem ipsum"
    // var inst = ABP.create( document.getElementById('load-player'), {
    //   'src': 'http://static.cdn.moe/ccltestingvideos/otsukimi_recital.mp4',
    //   'width': 600,
    //   'height': 400
    // });
    // CommentLoader('assets/otsukimi.xml', inst.cmManager);
    
  });
  $('#econ42button').on('click', function(){
    $('li').removeClass('active-li');
    $(this).parent().addClass('active-li');
    document.getElementById('youtube-video').innerHTML = '<iframe width="640" height="360" src="//www.youtube.com/embed/h-a6qOmkdl8" frameborder="0" allowfullscreen></iframe>'
    $('.video-intro-container').show()
    $('.course-desc').show()

    document.getElementById('below-title').innerHTML = "Video 2: 会计分录方法";
    document.getElementById('below-desc').innerHTML = "Last course we introduced the assets, liabilities and owner’s equities. We are going to learn the basic transaction and do the general journal in the accounting. How to get As in the first mid term?";
    document.getElementById('below-summ').innerHTML = "1. 会计分录，会计账户复习回顾（请大家务必把会计账户背熟！！记住什么属于asset,什么属于liability）Asset=liabilities+owners’equities<br/>2. 会计transactions,具体做帐方式，案例分析<br/>3. 灵活运用第一节课的知识点（第一个期中考试重要考点cover";
    document.getElementById('video-intro-class-name').innerHTML = "Class Name: Econ4, Principle of Accounting (Basic Introduction)";
    document.getElementById('video-intro-moorgee').innerHTML = "Moorgee: Alex (冬菇弟弟) ";
    document.getElementById('video-intro-moorgee').setAttribute("data-original-title", "如果在讲课当中大家发现冬菇弟弟有任何出错的地方，请大家毫不留情的指出来，我一定会在下面的准备中努力提高，为大家准备更有质量的辅助视频，谢谢大家。");
    // var inst = ABP.create( document.getElementById('load-player'), {
    //   'src': 'http://static.cdn.moe/ccltestingvideos/otsukimi_recital.mp4',
    //   'width': 600,
    //   'height': 400
    // });
    // CommentLoader('assets/otsukimi.xml', inst.cmManager);
    
  });
});


