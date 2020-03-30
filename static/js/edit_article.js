$(document).ready(function () {

    var editor = new Editor();
    editor.render();

    $("#select_game_div").children('a').click(function (e) {
        e.preventDefault();
        $('#selected_game').text($(this).text());
    });

    $("#exit_edit_btn").click(function (e) {
        e.preventDefault();
        window.location.href = $(this).attr('data-url');
    });

    $("#post_article_btn").click(function (e) {
        e.preventDefault();

        let article_id = $(this).attr('data-articleid');
        let article_title = $('#input_article_title').val();
        let article_content = editor.codemirror.getValue();
        let game_title = $('#selected_game').text().trim();
        if(article_title.length == 0) {
            alert('The article title is empty!');
            return;
        } else if(article_content.length == 0) {
            alert('The article content is empty!');
            return;
        } else if(game_title.length == 0) {
            alert('Please selete a game!');
            return;
        }

        if(!confirm('Are you sure you want to post this article?')) return;

        let csrftoken = getCookie('csrftoken');

        let send_items = {'id': article_id, 
                        'title': article_title, 
                        'content': article_content, 
                        'game_title': game_title, 
                        'csrfmiddlewaretoken': csrftoken}

        $.post("/gamers_havn/edit_article/", send_items, data => {
            window.location.href = data
        });
    });

});