$(document).ready(function () {
    
    let button_active = 'bg-primary text-light'

    $('#like_btn').click(function (e) { 
        e.preventDefault();
        
        if($(this).hasClass(button_active)) return;

        let article_id = $(this).attr('data-articleid');
        let button = $(this).text().trim();

        $.get("/gamers_havn/like_article/", {'article_id': article_id, 'button': button}, data => {
            $('#like_count').html(data);
            $(this).addClass(button_active);
            $('#dislike_btn').removeClass(button_active);
        });
    });

    $('#dislike_btn').click(function (e) { 
        e.preventDefault();
        
        if($(this).hasClass(button_active)) return;

        let article_id = $(this).attr('data-articleid');
        let button = $(this).text().trim();

        $.get("/gamers_havn/like_article/", {'article_id': article_id, 'button': button}, data => {
            $('#like_count').html(data);
            $(this).addClass(button_active);
            $('#like_btn').removeClass(button_active);
        });
    });

});