$(document).ready(function () {
    
    let button_active = 'bg-primary text-light'

    $('#like_btn').click(function (e) { 
        e.preventDefault();

        let article_id = $(this).attr('data-articleid');
        let button = $(this).text().trim();

        $.get("/gamers_havn/like_article/", {'article_id': article_id, 'button': button}, data => {
            if(data != -1) {
                $('#like_count').html(data);
                if(!$(this).hasClass(button_active)) {
                    $(this).addClass(button_active);
                    $(this).find('span').text("Liked");
                } else {
                    $(this).removeClass(button_active);
                    $(this).find('span').text("Like");
                }
            }
        });
    });

    $('#follow_btn').click(function (e) { 
        e.preventDefault();

        let game_id = $(this).attr('data-gameid');
        let button = $(this).text().trim();

        $.get("/gamers_havn/follow_game/", {'game_id': game_id, 'button': button}, data => {
            if(data) {
                if(!$(this).hasClass(button_active)) {
                    $(this).addClass(button_active);
                    $(this).find('span').text("Followed");
                } else {
                    $(this).removeClass(button_active);
                    $(this).find('span').text("Follow");
                }
            }
        });
    });

});