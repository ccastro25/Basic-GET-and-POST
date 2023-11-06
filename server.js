
const queryMysql = require('./mysqlconnection');
const express = require('express');

const app = express();
const bodyParser = require('body-parser');

// Create application/x-www-form-urlencoded parser
let urlencodedParser = bodyParser.urlencoded({ extended: false })

app.use(express.static('public'))
app.get('/index.html', function(req,res){

    console.log("testing form node") 
    //res.sendFile(__dirname + "/" +"index.html")
})

app.get('/process_get', function (req, res) {
    // Prepare output in JSON format
    
    response = queryMysql();
 
    response = {
        first_name:"castr",
        last_name:"bon"
     };
     console.log(response);
     res.end(JSON.stringify(response));
   
 })

let server = app.listen(8081, function () {
   let host = server.address().address
   let port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})