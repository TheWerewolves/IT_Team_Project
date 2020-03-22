$(document).ready(function () {
    
    $('#edit_profile_btn').click(function (e) { 
        if($(this).html() == "Edit Profile") {
            e.preventDefault();
            $('#edit_portrait').removeClass('d-none');
            $('#input_change_name').attr('readonly', false);
            $('#input_change_age').attr('readonly', false);
            $('#input_change_email').attr('readonly', false);
            $(this).html('Submit');
        }
    });

});