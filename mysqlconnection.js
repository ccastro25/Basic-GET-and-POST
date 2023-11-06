
module.exports =function connectToMysql(){
    let mysql = require('mysql2');
    let connec = mysql.createConnection({
        host :'localhost',
        user: 'castro',
        password:'jnfh(*89LJd267*&ldkj',
        database:'comparableproductsdb'
                  
    });

    connec.connect();
    connec.query('select * from walmartproducts',
                    function(error, results, fields){
                    if (error) throw error;
                    mysqlResulst = results;
                    console.log("results: ", results)
                    });

    connec.end();
    return mysqlResulst;
                }
