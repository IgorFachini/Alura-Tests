var http = require('http');

var config = {
    hostname: 'localhost',
    port:3000,
    path: '/produtos',
    headers: {//formato de resposta  que eu quero receber
        'Accept': 'application/json',
    }
};

http.get(config, function(res) {
    console.log(res.statusCode);
    console.log(res.body);

    res.on('data', function (body) {
        console.log('BODY: ' + body);
    });
});