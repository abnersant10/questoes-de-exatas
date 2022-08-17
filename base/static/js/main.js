$(document).ready(function(){
    $(".btn").click( function () {
        $.ajax({
            url : '{{assunto}}',
            type: 'get',
            // data é tudo que vou enviar para o servidor
            // ex enviar o texto do botão
            data:{
                button_text: $(this).text(),


            },
            // é o que acontecerá quando o servidor responder com sucesso
            // neste exemplo alterar o texto do butão
            success: function (response){

                $(".btn").text(response.seconds)
                $("#seconds").append('<p>'+response.seconds +'</p>')
                $("#id_enunciado").append('<p>'+response.id_enunciado+'</p>')
            }
        });
    });
});