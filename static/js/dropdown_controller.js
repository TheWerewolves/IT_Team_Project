$(document).ready(function () {

    $('#search_type_dropdown a').click(function (e) { 
        e.preventDefault();
        $(this).parent().siblings('button').text($(this).text());
        $(this).parent().siblings('input').val($(this).text());
    });
    
});