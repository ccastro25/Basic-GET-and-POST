const mysql = require('mysql2/promise');
module.exports = async function getSqlRows() {
    
    // create the connection
    const connection = await mysql.createConnection({host:'localhost', user: 'castro',
                                                    password:'jnfh(*89LJd267*&ldkj',database:'comparableproductsdb'});
    // query database
    const [rows, fields] = await connection.execute('select * from walmartproducts');
    connection.end();
    return rows
    }