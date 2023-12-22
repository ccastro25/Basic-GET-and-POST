stores = [ 'walmartproducts', 'shopriteproducts', 'cvsproducts', 'riteaidproducts', 'acmeproducts'] 

const mysql = require('mysql2/promise');

module.exports = async function getSqlRows(searchTerm) {
  // create the connection
  const connection = await mysql.createConnection({
    host: 'localhost',
    user: 'castro',
    password: 'jnfh(*89LJd267*&ldkj',
    database: 'comparableproductsdb'
  });

  try {
    // query database with parameterized query
    const queryStatement = `
      SELECT * FROM walmartproducts WHERE product_name LIKE ? 
      UNION ALL 
      SELECT * FROM cvsproducts WHERE product_name LIKE ? 
      UNION ALL 
      SELECT * FROM riteaidproducts WHERE product_name LIKE ? 
      UNION ALL 
      SELECT * FROM shopriteproducts WHERE product_name LIKE ? 
      UNION ALL 
      SELECT * FROM acmeproducts WHERE product_name LIKE ?;`;

    const [rows, fields] = await connection.execute(queryStatement, [
      `%${searchTerm}%`,
      `%${searchTerm}%`,
      `%${searchTerm}%`,
      `%${searchTerm}%`,
      `%${searchTerm}%`,
    ]);

    return rows;
  } finally {
    // close the connection in a 'finally' block to ensure it happens regardless of success or failure
    connection.end();
  }
};
