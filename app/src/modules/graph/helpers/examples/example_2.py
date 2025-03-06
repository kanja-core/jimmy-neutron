example_2 = """
human: I want to download my national tax certificate, my cpf is 527.281.628.59;
The website is: solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/pf;

    input: (
           

            <!DOCTYPE html>
            <html>
            <head>
                <meta content="IE=edge" http-equiv="X-UA-Compatible" />
                <meta charset="utf-8" />
                <title>Certid&#227;o de D&#233;bitos Relativos a Cr&#233;ditos Tribut&#225;rios Federais e &#224; D&#237;vida Ativa da Uni&#227;o</title>
                <script src="/Servicos/certidaointernet/Scripts/jquery-3.3.1.js"></script>
                <script src="/Servicos/certidaointernet/Scripts/jquery.maskedinput.js"></script>
                <script src="/Servicos/certidaointernet/Scripts/jquery.validate.min.js"></script>
                <script src="/Servicos/certidaointernet/Scripts/site.js?t=638763328866405128"></script>
                <script src="/Servicos/certidaointernet/Scripts/jquery.filedownload.js?t=638763328866405128"></script>
                <script src="/Servicos/certidaointernet/Scripts/jquery-ui.js"></script>
                <link rel="stylesheet" href="/tema/css/rfb.css">
                <link href="/Servicos/certidaointernet/Content/jquery-ui.css" rel="stylesheet" />
                <link href="/Servicos/certidaointernet/Content/Site.css?t=638763328866405128" rel="stylesheet" />
                <link href="/Servicos/certidaointernet/Content/material-icons.css" rel="stylesheet" />    
                <script data-main="//servicos.receita.fazenda.gov.br/tema/main-built.js" src="//servicos.receita.fazenda.gov.br/tema/require.js"></script>
                <script src="//www.receita.fazenda.gov.br/estatistica/estatistica.js"></script>
                
            </head>
            <body>
                <div id="rfb-main-container">
                    <div class="parametros group-inline">
                            <h1 class="documentFirstHeading">Certid&#227;o de D&#233;bitos Relativos a Cr&#233;ditos Tribut&#225;rios Federais e &#224; D&#237;vida Ativa da Uni&#227;o</h1>
                        <!--  O conteúdo da página deve ser inserido aqui  -->
                        


            <h3>Emissão da Certidão</h3>

            <form action="/Servicos/certidaointernet/pf/emitir/Verificar" id="frmInfParam" method="post">Da certidão emitida por meio da internet constará, obrigatoriamente, a hora, a data da emissão e o código de controle<br /><br />Base Legal: <a href="JavaScript:AbrirLei()">Portaria RFB/PGFN n° 1.751, de 02/10/2014</a>.    <div class="linha" style="padding-top: 8px;">
                    <div class="espaco">
                        O número do CPF deve ser informado incluindo-se os 11 dígitos numéricos.
                    </div>
                </div>
                <div class="linha">
                    <div class="espaco">
                        <div>
                            <b>Informe o CPF:</b> 
                        </div>
                        <div>
                            <input autocomplete="off" class="pular submit" data-proximo="Captcha" id="NI" maxlength="14" name="NI" style="width:110px" tabindex="1" type="text" value="" />
                        </div>
                    </div>
                </div>
                <div class="espaco" style="padding-bottom: 0px">
                    
                    <button class='h-captcha botao-captcha' data-sitekey='4a65992d-58fc-4812-8b87-789f7e7c4c4b' data-callback='submit'>Hcaptcha</button><script src='https://js.hcaptcha.com/1/api.js?recaptchacompat=off&hl=pt-BR' async defer></script>
                    <input type="button" value="Consultar" id="validar" name="validar" class="pular" tabindex="4" />
                    <input type="button" value="Limpar" id="limpar" name="limpar" class="pular" tabindex="5" />
                </div>
            </form>

                        
                    </div>
                </div>
                <div class="modalLoading" hidden>
                </div>

                <div id="dialog-message" title="Emiss&#227;o da Certid&#227;o" hidden>
                    <span class="ui-icon ui-icon-alert" style="float: left; margin: 0px 12px 50px 0; "></span>
                    <div style="margin-left: 28px;"><p><span id="mensagem"></span></p></div>
                </div>

                <div id="modal-avaliacao" style="padding: 0px">
                </div>

                
                <script type="text/javascript">function submit() { $('form').submit(); }</script>

                <script type="text/javascript">
                    var ni;

                    //Validações
                    $.validator.addMethod('validarNI',
                        function (value, element) {
                            ni = $("#NI").val();
                            return validarCPF(ni);
                        });

                    //Validação tamanho campo
                    $.validator.addMethod('validarTamanhoNI',
                        function (value, element) {
                            ni = $("#NI").val();
                            return validarTamanhoNumeroImovel(ni);
                        });

                    $('#IdentificadorAfericao').blur(function () {
                        if ($(this).val() != '') {
                            $(this).val(("000" + $(this).val()).slice(-3));
                        }
                    });

                    (function () {
                        $('#validar').on("click", function () {
                            formataCPF('NI');
                            var form = $("#frmInfParam");

                            if ($('#IdentificadorAfericao').val() != "") {
                                $('#IdentificadorAfericao').val(("000" + $('#IdentificadorAfericao').val()).slice(-3));
                            }

                            var validator = form.validate();

                            var fieldsToValidate = ['#NI', '#IdentificadorAfericao', '#Captcha'];

                            for (var i = 0; i < fieldsToValidate.length; i++) {
                                for (var j = 0; j < $(fieldsToValidate[i]).length; j++) {
                                    var elemento = $(fieldsToValidate[i])[j];
                                    if (!validator.element($(elemento))) {
                                        return;
                                    }
                            }
                            }

                            setCookie("fileDownload", "", -1, "/");
                            setTimeout(setTimer, 200);
                            $(".botao-captcha").click();
                    });

                        function setTimer() {
                            //cookie existe
                            if (getCookie("fileDownload") != "") {
                                window.location = '/Servicos/certidaointernet/pf/emitir';
                            }
                            else {
                                setTimeout(setTimer, 200);
                            }
                        }

                        $('#frmInfParam').submit(function () {
                            $("#validar").prop('disabled', true);
                            return true;
                        });

                        $('#NI').mask('999.999.999-99', { autoclear: false, placeholder: "" });
                        $('#IdentificadorAfericao').mask('999', { autoclear: false, placeholder: "" });

                        $('#NI').blur(function () {
                            formataCPF('NI');
                        });

                        $('input.pular').bind('paste', function () { $(this).val(''); });

                        //Pular automaticamente para o próximo quando terminar de digitar o valor
                        $('.pular').keyup(function (e) {
                            if ($(this).val().length == $(this).prop('maxlength')) {
                                $('#' +  $(this).attr("data-proximo")).focus();
                            }
                        });

                        $("#limpar").on("click", function () {
                            $("#NI").val('');
                            $("#IdentificadorAfericao").val('');
                            $("#Captcha").val('');
                            $('#recarregar').trigger('click');
                            $("#validar").prop('disabled', false);
                            $("#NI").focus();
                        });

                        //Validaçao
                        $('#frmInfParam').validate({
                            onsubmit: false, //ignora validação do form ao chamar o método .submit
                            debug: false,
                            rules: {
                                NI: {
                                    required: true,
                                    validarTamanhoNI: true, 
                                    validarNI: true
                                },
                                IdentificadorAfericao: {
                                    required: true
                                },
                                Captcha: {
                                    required: true
                                }
                            },
                            messages: {
                                NI: {
                                    required: 'CPF não informado',
                                    validarTamanhoNI: '',
                                    validarNI:'CPF inválido'
                                },
                                IdentificadorAfericao: {
                                    required: 'A aferição de obra informada está incorreta.'
                                },
                                Captcha: {
                                    required: 'Digite corretamente os caracteres da imagem.'
                                }
                            },
                            onkeyup: null,
                            focusInvalid: false,
                            onfocusout: false,
                            onclick: false,
                            errorPlacement: function (error, element) {
                                MensagemAlerta(error.text(), element);
                                $("#validar").prop('disabled', false);
                            }
                        });
                    }
                )()

                $(document).ready(function () {

                    $("#validar").prop('disabled', false);
                });

                $('.submit').keypress(function (e) {
                    if (e.which == 13) {
                        
                        e.preventDefault();
                        
                        $("#validar").focus();
                        $('#validar').trigger('click');
                        return false;
                    }
                    });
                </script>

            </body>
            </html>,

            

            <!DOCTYPE html>
            <html>
            <head>
                <meta content="IE=edge" http-equiv="X-UA-Compatible" />
                <meta charset="utf-8" />
                <title>Certid&#227;o de D&#233;bitos Relativos a Cr&#233;ditos Tribut&#225;rios Federais e &#224; D&#237;vida Ativa da Uni&#227;o</title>
                <script src="/Servicos/certidaointernet/Scripts/jquery-3.3.1.js"></script>
                <script src="/Servicos/certidaointernet/Scripts/jquery.maskedinput.js"></script>
                <script src="/Servicos/certidaointernet/Scripts/jquery.validate.min.js"></script>
                <script src="/Servicos/certidaointernet/Scripts/site.js?t=638763329157203961"></script>
                <script src="/Servicos/certidaointernet/Scripts/jquery.filedownload.js?t=638763329157203961"></script>
                <script src="/Servicos/certidaointernet/Scripts/jquery-ui.js"></script>
                <link rel="stylesheet" href="/tema/css/rfb.css">
                <link href="/Servicos/certidaointernet/Content/jquery-ui.css" rel="stylesheet" />
                <link href="/Servicos/certidaointernet/Content/Site.css?t=638763329157203961" rel="stylesheet" />
                <link href="/Servicos/certidaointernet/Content/material-icons.css" rel="stylesheet" />    
                <script data-main="//servicos.receita.fazenda.gov.br/tema/main-built.js" src="//servicos.receita.fazenda.gov.br/tema/require.js"></script>
                <script src="//www.receita.fazenda.gov.br/estatistica/estatistica.js"></script>
                
                <style>
                    table {
                        border-spacing: 0;
                        border-collapse: separate;
                        width: 100%;
                        border: none;
                    }

                    span {
                        font-size: 13px;
                        font-family: Arial;
                    }

                    .center {
                        margin: auto;
                    }
                </style>

            </head>
            <body>
                <div id="rfb-main-container">
                    <div class="parametros group-inline">
                            <h1 class="documentFirstHeading">Certid&#227;o de D&#233;bitos Relativos a Cr&#233;ditos Tribut&#225;rios Federais e &#224; D&#237;vida Ativa da Uni&#227;o</h1>
                        <!--  O conteúdo da página deve ser inserido aqui  -->
                        



            <h3></h3>

            <form action="/Servicos/certidaointernet/pf/emitir/Verificar" id="FrmSelecao" method="post">    <br />&nbsp;<br />
                <a href="/Servicos/certidaointernet/pf/Consultar?ni=52728162859&amp;TipoPesquisa=1&amp;PeriodoInicio=2024-09-01&amp;PeriodoFim=2025-02-28">Consulta de certid&atilde;o e emiss&atilde;o de 2&ordf; via</a>
                <br />&nbsp;<br />
                <a href="/Servicos/certidaointernet/pf/Emitir/EmProcessamento?Ni=52728162859">Emiss&atilde;o de nova certid&atilde;o</a>
                <br />&nbsp;<br />
                <br /> <br />
                <div class="center" style="width:100%;text-align: center; margin-left: -32px;">
                    <input type="button" value="Página Inicial" name="PaginaInicial" onclick="document.location = '/Servicos/certidaointernet/pf/emitir'">
                </div>
            </form>
                        
                    </div>
                </div>
                <div class="modalLoading" hidden>
                </div>

                <div id="dialog-message" hidden>
                    <span class="ui-icon ui-icon-alert" style="float: left; margin: 0px 12px 50px 0; "></span>
                    <div style="margin-left: 28px;"><p><span id="mensagem"></span></p></div>
                </div>

                <div id="modal-avaliacao" style="padding: 0px">
                </div>

                
            </body>
            </html>


    );
    The output should be:
    [
        {
            type: 'disableAutoSolve',
            cat: 'captcha',
        },
        {
            type: 'goto',
            cat: 'default',
            selector: solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/pf,
        },
        {
            type: 'screenshot',
            cat: 'default',
            value: 'img/start.png',
        },
        {
            type: 'input',
            cat: 'default',
            selector: '#NI',
            value: '15358587888',
        },
        {
            type: 'screenshot',
            cat: 'debug',
            value: 'img/form.png',
        },
        {
            type: 'wait',
            cat: 'default',
            timeout: 500,
        },
        {
            type: 'solve',
            cat: 'captcha',
        },
        {
            type: 'screenshot',
            cat: 'debug',
            value: 'img/captcha.png',
        },
        {
            type: 'wait',
            cat: 'default',
            timeout: 1000,
        },
        {
            type: 'screenshot',
            cat: 'debug',
            value: 'img/end.png',
        },
        {
            type: 'download',
            cat: 'default',
            selector: '/Servicos/certidaointernet/pf/Emitir/EmProcessamento',
            value: '/tmp/file.pdf',
        },
    ];
"""
