$(document).ready(function() {
    $('.myForm').ajaxForm(function(response) {
        $('.formMainModal').modal('hide');
        $('#successModal').modal('show');
        $('.datas').val('');
    });
});
