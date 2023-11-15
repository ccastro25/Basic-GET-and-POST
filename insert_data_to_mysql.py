from datetime import date, datetime, timedelta
import mysql.connector
def insert_data(product_name, price)
  cnx = mysql.connector.connect(user='castro', password ='jnfh(*89LJd267*&ldkj',database='comparableproductsdb')
  cursor = cnx.cursor()

  today = datetime.now().date()

  today = tomorrow = datetime.now().date()

  add_products = { "INSERT INTO walmartpoducts"
                  "(product_name, price, date)"
                  "VALUES(%(product_name)s,%(price)s,%(date)s)"
  }
  data_products =(product_name,price,today)
  cursor.execute(add_products,data_products)

  cnx.commit()

  cursor.close()
  cnx.close()