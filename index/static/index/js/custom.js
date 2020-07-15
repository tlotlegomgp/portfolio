$(document).ready(function() {

    //Get header height
    var headerHeight = $('nav').outerHeight();
    $('.slide-section').click(function(e) {
  
      var linkHref = $(this).attr('href');
  
      $('html, body').animate({
        scrollTop: $(linkHref).offset().top - (headerHeight)
      }, 800);
  
      e.preventDefault();
    });
  });