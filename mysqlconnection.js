let mysql = require('mysql2');

let mysqlResults; 
module.exports =function connectToMysql(){
    





    const connec = mysql.createConnection({
        host :'localhost',
        user: 'castro',
        password:'jnfh(*89LJd267*&ldkj',
        database:'comparableproductsdb'
                  
    });

    connec.connect();
    let q = connec.query('select * from walmartproducts');
    
    connec.end();
    return q;
                }
