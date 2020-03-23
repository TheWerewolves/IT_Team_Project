$(document).ready(function () {

    var editor = new Editor();
    editor.render();  

    $("#exit_edit_btn").click(function (e) {
        e.preventDefault();
        window.location.href = $(this).attr('data-url');
    });

    $("#post_article_btn").click(function (e) {
        e.preventDefault();

        let article_title = $('#input_article_title').val();
        let article_content = editor.codemirror.getValue();
        if(article_title.length == 0) {
            alert('The article title is empty!');
            return;
        } else if(article_content.length == 0) {
            alert('The article content is empty!');
            return;
        }

        if(!confirm('Are you sure you want to post this article?')) return;

        let csrftoken = getCookie('csrftoken');

        $.post("/gamers_havn/edit_article/", {'title': article_title, 'content': article_content, 'csrfmiddlewaretoken': csrftoken}, data => {
            window.location.href = data
        });
    });

});