Site = {
    url_service: "/service/",

    // buscando os hotes
    getHoteis: function (arg) {

        var service = Site.url_service + "get-disponibilidade/"

        jQuery('.loader').css('display', 'block')
        jQuery('.resultado-busca').css('display', 'none')
        jQuery('#BoxResutado').html("")

        $.ajax({
            url: service,
            dataType: 'json',
            data: arg
        }).done(function (response) {
            var html = '';

            if (response.length == 0) {
                jQuery('#BoxResutado').html('<h3>Nenhum registro encontrado.</h3>');
                jQuery('.resultado-busca').css('display', 'block')
                jQuery('.loader').css('display', 'none')

            }

            $.each(response, function (i, item) {

                html += '<tr>';
                html += '<td>' + item.nome + '</td>';
                html += '<td>' + item.cidade + '</td>';
                html += '<td>' + item.data + '</td>';
                html += '<td>' + item.vagas + '</td>';
                html += '<td>' + item.noites + '</td>';
                html += '</tr>';

                jQuery('#BoxResutado').html(html);
                jQuery('.loader').css('display', 'none')
                jQuery('.resultado-busca').css('display', 'block')
            })

        });
    },


    // iniciando o search
    setSearchSelect: function () {

        var URL = Site.url_service + "get-hoteis/";

        $("#HoteisList").select2({
           
   
            tokenSeparators: [',', ' '],
            minimumInputLength: 2,
            minimumResultsForSearch: 10,
            ajax: {
                url: URL,
                dataType: "json",
                type: "GET",
                data: function (params) {

                    var queryParameters = {
                        term: params.term
                    }
                    return queryParameters;
                },
                processResults: function (data) {
                    return {
                        results: $.map(data, function (item) {
                            return {
                                text: item.cidade + " - " + item.nome,
                                id: item.id
                            }
                        })
                    };
                }
            }
        });
    },

    // iniciando o calendario
    setDatePicker: function () {
        jQuery('.data-inicio').datepicker({ format: 'd-m-yyyy' });
        jQuery('.data-fim').datepicker({ format: 'd-m-yyyy' });
    },


    setForm: function () {

        jQuery("#Formulario").submit(function (ev) {
            ev.preventDefault();

            var dados = { idhotel: null, data_inicio: null, data_fim: null, todos: null };

            dados.idhotel = $(".idhotel").val();
            dados.data_inicio = $(".data-inicio").val();
            dados.data_fim = $(".data-fim").val();
            dados.todos = $(".sem-data").is(":checked")

            if (!dados.todos && (dados.data_inicio === "" || dados.data_fim === "")) {

                jQuery('#ModalAviso').modal('show')
                return false;
            }

            Site.getHoteis(dados);

        });



    },

    // init do objeto site
    init: function () {
        //this.getHoteisCidades();
        this.setSearchSelect();
        this.setDatePicker();
        this.setForm();
    }
    
}

jQuery(document).ready(function () {
    Site.init();
})