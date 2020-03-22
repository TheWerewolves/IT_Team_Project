$(document).ready(function () {
    
    feather.replace();

    var editor = new Editor();
    editor.render();  

    $("#postBtn").click(function () {
        alert(editor.codemirror.getValue());
    });

});