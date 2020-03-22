$(document).ready(function () {

    $('#search_input').keyup(function(e) {
        if (e.keyCode === 13) {
            e.preventDefault();
            $("#search_btn").click();
        }
    });
    
});