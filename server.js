var express = require('express');
var app = express();
var bodyParser = require('body-parser');

// Create application/x-www-form-urlencoded parser
var urlencodedParser = bodyParser.urlencoded({ extended: false })

app.use(express.static('public'))
app.get('/index.html', function(req,res){
    res.sendFile(__dirname + "/" +"index.html")
})

app.post('/process_post', urlencodedParser, function (req, res) {
    // Prepare output in JSON format
    response = {
       first_name:req.body.first_name,
       last_name:req.body.last_name
    };
    console.log(response);
    res.end(JSON.stringify(response));
 })

app.get('/process_get', function (req, res) {
    // Prepare output in JSON format
    response = {
       first_name:req.query.first_name,
       last_name:req.query.last_name
    };
    console.log(response);
    res.end(JSON.stringify(response));
 })

// This responds with "hellow word" on the homepage
app.get('/', function (req, res) {
   console.log("Got a GET request for the homepage");
   res.send('Hello GET');
})

// this reponds a post request for the homepage
app.post('/', function(req, res){
    console.log("Got a post request for the homepage");
    res.send('Hello Post');
})

//this reponds a Delete rquest for the del_user page
app.delete('del_user',function(req, res){
    console.log("goot a delete rquest for /del_user");
    res.send('Page listing');
})

//this responds a get request for the /list_user page
app.get('/list_user', function(req, res){
    console.log("Got a get request for /list_user");
    res.send('Page Listing');
})

//This respnds a get request for abcd, abxcd, ab123cd, and so on 
app.get('/ab*cd', function(req,res){
    console.log("Got a Get request for /ab*cd");
    res.send('Page Pattern Match');
})



var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})