import mysql.connector
#table creation  CREATE TABLE walmartproducts (id INT not null auto_increment, product_name VARCHAR(30),price DECIMAL(5,2), the_date DATE, primary key(id));

def insert_data(seq_of_params):
    cnx = mysql.connector.connect(user='castro', password ='jnfh(*89LJd267*&ldkj',database='comparableproductsdb')
    cursor = cnx.cursor()

    add_products =  "INSERT INTO walmartproducts(product_name, price, the_date) VALUES(%s,%s,%s)"
    
   
    cursor.executemany(add_products,seq_of_params)

    cnx.commit()

    cursor.close()
    cnx.close()

