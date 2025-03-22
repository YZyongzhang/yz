const http = require('http');
// import http
const hostname  = '127.0.0.1';

const port  = 3000;

const server = http.createServer((req , res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type' , 'text/plain');
    res.end('hello world\n');
});

server.listen(port , hostname, () => {
    console.log(`server runing at http://${hostname}:${port}/`);
    
});