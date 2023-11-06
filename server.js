
const queryMysql = require('./mysqlconnection');
const express = require('express');
const domResults = require('./getDomContents')
const app = express();

// Create application/x-www-form-urlencoded parser
let urlencodedParser = bodyParser.urlencoded({ extended: false })

app.use(express.static('public'))
app.get('/index.html', function(req,res){
    domResults();
    console.log("testing form node") 
    //res.sendFile(__dirname + "/" +"index.html")
})


app.get('/process_get', function (req, res) {
    // Prepare output in JSON format
    
    response = queryMysql();
 
    queryMysql();
    res.end(response);
    domResults();
   
 })


let server = app.listen(8081, function () {
   let host = server.address().address
   let port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})