module.exports = function(app) {
    app.get("/",function(req, res) {
        var connection = app.infra.connectionFactory();
        var produtos = new app.infra.ProdutoDao(connection);
        console.log("ola");
        produtos.lista(function(error,results,fields){
            res.render('home/index',{livros:results});
            console.log("ola2",results);

        });
        connection.end();

    });
}