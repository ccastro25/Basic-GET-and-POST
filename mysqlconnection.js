const mysql = require('mysql2/promise');
module.exports = async function getSqlRows(searchTerm) {
    console.log("this is the term " +searchTerm)
    // create the connection
    const connection = await mysql.createConnection({host:'localhost', user: 'castro',
                                                    password:'jnfh(*89LJd267*&ldkj',database:'comparableproductsdb'});
    // query database
    let queryStatement = "select * from walmartproducts where productname like '%"+searchTerm+"%'"
    const [rows, fields] = await connection.execute(queryStatement);
                                                   
    console.log("these are the rows "+rows)
    connection.end();
    return rows
    }