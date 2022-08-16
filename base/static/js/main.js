$(document).ready(function(){
    $(".btn").click( function () {
        $.ajax({
                url: '{{assunto}}',
                type: 'get',
                data: {
                    button_text: $(this).text()
                },
                success: function (response){
                    $(".btn").text(response.seconds)
                }
        });
    });
});