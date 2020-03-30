$(document).ready(function () {
    
    let button_active = 'bg-primary text-light'

    $('#orderby_div').find('button').click(function (e) { 
        e.preventDefault();

        if($(this).hasClass(button_active)) return;

        let game_id = $(this).parent().attr('data-gameid');
        let orderby = $(this).text().trim();

        $.get("/gamers_havn/game_list_article/", {'game_id': game_id, 'orderby': orderby}, data => {
            if(data == null) return;
            $('#article_list_div').html(data);
            $(this).addClass(button_active);
            $(this).siblings().removeClass(button_active);
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