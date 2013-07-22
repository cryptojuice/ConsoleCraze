$(document).ready(function() {

    $('ul.nav li a').on('click', function(e) {
        $('ul.nav li.active').removeClass('active')
        $(this).parent('li').addClass('active');
    });

});
