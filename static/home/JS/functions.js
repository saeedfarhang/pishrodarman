// jquerySlider

$(document).ready(function() {
    console.log("ready!");
    $('.slide:eq(0)').addClass('active');

});


setInterval(function() {
    // console.log('h');
    var currentSlide = $('.slide.active');
    var nextSlide = currentSlide.next();
    currentSlide.addClass('active');
    currentSlide.removeClass('active');
    nextSlide.addClass('active');

    if (nextSlide.length == 0) {
        $('.slide').first().addClass('active');
    }
}, 4000);