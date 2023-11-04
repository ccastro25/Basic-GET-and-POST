const puppeteer = require('puppeteer');
const queryMysql = require('./mysqlconnection');
const express = require('express');
const app = express();
const bodyParser = require('body-parser');

// Create application/x-www-form-urlencoded parser
let urlencodedParser = bodyParser.urlencoded({ extended: false })

app.use(express.static('public'))
app.get('/index.html', function(req,res){
    res.sendFile(__dirname + "/" +"index.html")
})

app.post('/process_post', urlencodedParser, function (req, res) {
    // Prepare output in JSON format
    let div = document.getElementById("result")
    response = {
       first_name:req.body.first_name,
       last_name:req.body.last_nam
    };
    div.innerText = 
    console.log(response);
    res.end(JSON.stringify(response));
 })

 

app.get('/process_get', function (req, res) {
    // Prepare output in JSON format
    
    response = queryMysql();
 
   
    queryMysql();
    res.end(response);
    pup()
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






async function pup() {
    const browser = await puppeteer.launch();
    page = await browser.newPage();
        await page.goto('file:///Users/caonabocastro/Desktop/basicRouting/BasicGetAndPost/index.html', {waitUntil: 'load'});


    const newPage = await page.evaluate(() => {

        return  document.getElementById("result").innerText;

        });

     console.log(newPage)
  
    await browser.close();
  };

let server = app.listen(8081, function () {
   let host = server.address().address
   let port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})