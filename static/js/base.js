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
        let a = $(this).parent().siblings('a');
        a.children('span').text($(this).text());
        a.children('input').val($(this).text());
    });
    
});