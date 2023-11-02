module.exports =function connectToMysql(){
    let mysql = require('mysql2');
    let connec = mysql.createConnection({
        host :'localhost',
        user: 'c',
        password:'p',
        database:'comparableproductsdb'
                  
    });

    connec.connect();
    connec.query('select * from walmartproducts',
                    function(error, results, fields){
                    if (error) throw error;
                    console.log("results: ", results)
                    });

    connec.end();
                }
