import mysql.connector
#table creation  CREATE TABLE walmartproducts (id INT not null auto_increment, product_name VARCHAR(30),price DECIMAL(5,2), the_date DATE, primary key(id));

def insert_data(product_name, price,today):
    cnx = mysql.connector.connect(user='castro', password ='jnfh(*89LJd267*&ldkj',database='comparableproductsdb')
    cursor = cnx.cursor()

    add_products = { "INSERT INTO walmartpoducts"
                    "(product_name, price, date)"
                    "VALUES(%(product_name)s,%(price)s,%(date)s)"
    }
    data_products =(product_name,price,today)
    cursor.execute(add_products,data_products)

    cnx.commit()

    cursor.close()
    cnx.close()

