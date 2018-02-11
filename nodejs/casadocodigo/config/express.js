var express = require('express');
var load = require('express-load');// Carrega modulos automaticamente
var bodyParser = require('body-parser');
var expressValidator = require('express-validator');

module.exports = function() {

    var app = express();
    app.use(express.static('./public'));// arquivos estaticos, css,htmls,js etc, para q nao caia em rotas.
    app.set('view engine', 'ejs');
    app.set('views','./app/views');

    // extended, formularios q tem interligacao com outros dados,
    //  ex: (add bibliotecas -> livros) n sao entendidos mais, 
    // extended abilita o entendimento
    app.use(bodyParser.urlencoded({extended: true}));
    app.use(bodyParser.json());
    app.use(expressValidator());

    // carrega rotas(procura em todas aplicacao(cwd limita o local de procura))
    //  em app,depois carrega os de infra e deixa na var app, 
    load('routes',{cwd: 'app',verbose:true})
        .then('infra')
        .into(app);

    // midware nosso,
    app.use(function(req, res, next){
        res.status(404).render("erros/404");
    });

    app.use(function(error,req, res, next){
        console.log("nodeenv",process.env.NODE_ENV);
        if (process.env.NODE_ENV == 'production') {
            res.status(500).render("erros/500");
            return;
        }
        next(error);
    });
    //tem que colocar na ordem, caso contrário ele passa pelo middleware e ainda não vai ter acontecido nenhum erro.




    return app;
};
