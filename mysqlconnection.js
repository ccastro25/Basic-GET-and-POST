const mysql = require('mysql2/promise');
stores = [ 'walmartproducts', 'shopriteproducts', 'cvsproducts', 'riteaidproducts', 'acmeproducts'] 

module.exports = async function getSqlRows(searchTerm) {
    const connection = await mysql.createPool({host:'localhost', user: 'castro',
    password:'jnfh(*89LJd267*&ldkj',database:'comparableproductsdb'});
  
    try {
        let allRows = [];

        for (let i = 0; i < stores.length; i++) {
          const tableName = stores[i];
          const queryStatement = `SELECT * FROM ${tableName} WHERE product_name LIKE ?`;
          const [rows, fields] = await connection.execute(queryStatement, [`%${searchTerm}%`]);
          allRows.push({ tableName, rows });
        }
    
        return allRows;
      } finally {
        connection.release(); // Always release the connection, even if an error occurs
      }
  }

    