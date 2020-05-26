// Functionality for Navigation Bar on Scroll


   $(document).ready(navSizing);
   $(window).resize(navSizing);

    function navSizing() {
   
    var $nav = $("#mainNavbar");
    var width = $(window).width();
    var scroll = $(window).scrollTop();

    if (width >= 991 && scroll < $nav.height()) {
        $nav.removeClass("scrolled");
        $nav.toggleClass("navbar-dark");
        $nav.removeClass("navbar-light");
        $('.navbar .navbar-brand img').attr('src', '/static/img/logo-transparent.png')
    }
    else {
        $nav.toggleClass("scrolled");
        $nav.toggleClass("navbar-light");
        $nav.removeClass("navbar-dark");
        $('.navbar .navbar-brand img').attr('src', '/static/img/aloha-logo.png');
    }   

   }

$(function () {
    $(document).scroll(function () {
        var $nav = $("#mainNavbar");
        var width = $(window).width();
  
        $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
        $nav.toggleClass("navbar-light", $(this).scrollTop() > $nav.height());
        $nav.removeClass("navbar-dark", $(this).scrollTop() > $nav.height());
        $nav.toggleClass("navbar-dark", $(this).scrollTop() < $nav.height());

        $nav.toggleClass("navbar-light", width < 991);
        $nav.removeClass("navbar-dark", width < 991);

        if ($(window).width() <= 991) {
            $('.navbar .navbar-brand img').attr('src', '/static/img/aloha-logo.png');
        }

        if ($(this).scrollTop() > $nav.height() || ($(window).width() < 991)) {
            $('.navbar .navbar-brand img').attr('src', '/static/img/aloha-logo.png');
        }
        else {
            $('.navbar .navbar-brand img').attr('src', '/static/img/logo-transparent.png');
        }



    })
}); 
