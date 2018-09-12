(function (addr) {
var socket = new WebSocket('ws://'+addr+'/ws');

socket.onmessage = function(evt) {
    document.getElementById('main').innerHTML = evt.data;
};

socket.onerror = function(evt) {
    console.info('an error occurred: ' + evt);
};

socket.onopen = function(evt) {
    console.info('Connection established');

};

socket.onclose = function() {
    console.info('Connection closed');
    //document.getElementById('main').innerHTML = '<img src="/static/stand-by.jpg" alt="">';
    document.getElementById('main').innerHTML = 'Serviço Indisponível';
    window.setTimeout(attemptConnection, 1000);
};
return socket
})();