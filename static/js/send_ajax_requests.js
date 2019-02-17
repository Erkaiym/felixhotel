$(document).ready(function() {
    $('.myForm').ajaxForm(function(response) {
        $('.formMainModal').modal('hide');
        $('#successModal').modal('show');
        $('.datas').val('');
    });

    $('.reviewForm').ajaxForm(function(response) {
        $('.formMainModal').modal('hide');
        $('#successReviewModal').modal('show');
        $('.datas').val('');
    });
});
