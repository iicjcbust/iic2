$('.bar-percentage[data-percentage]').each(function () {
    var progress = $(this);
    var percentage = Math.ceil($(this).attr('data-percentage'));
    
    $({countNum: 0}).animate({countNum: percentage}, {
        
        duration: 10000,
      easing:'linear',  
      step: function() {


        var pct = Math.floor(this.countNum) + '%';
        progress.text(pct) && progress.siblings().children().css('width',pct);
      }
    });
  });