$(document).ready(function () {

    feather.replace();

    $('#search_input').keyup(function(e) {
        if (e.keyCode === 13) {
            e.preventDefault();
            $("#search_btn").click();
        }
    });

    $('#search_type_dropdown a').click(function (e) { 
        e.preventDefault();
        $(this).parent().siblings('a').children('span').text($(this).text());
        $(this).parent().siblings('input').val($(this).text());
    });
    
});