$(document).ready(function () {
    
    $('#edit_profile_btn').click(function (e) { 
        if($(this).html() == "Edit Profile") {
            e.preventDefault();
            $('#input_change_name').attr('readonly', false);
            $('#input_change_age').attr('readonly', false);
            $('#input_change_email').attr('readonly', false);
            $(this).html('Submit');
        }
    });

    $('#change_portrait_btn').click(function (e) { 
        e.preventDefault();
        
    });

    $('#search_input').keyup(function(e) {
        if (e.keyCode === 13) {
            e.preventDefault();
            $("#search_btn").click();
        }
    });
    
});