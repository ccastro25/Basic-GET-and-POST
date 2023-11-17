
from insert_data_to_mysql import insert_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from datetime import  datetime
   
today = datetime.now().date()

#eggs has to be searched as egg. some items have egg 
grocery_list =[
                'Egg',
                'Milk',
                'Bread',
                'Bacon',
                'Cooking+oil',
                'Rice',
                'Tuna',
                'Steak',
                'Chicken', 
                'Ham', 
                'Cheese',
                'Yogurt', 
                'Platano',
                'Frozen+pizza'
                'Grapes',
                'Strawberry',
                'Blueberry', 
                'Raspberry',
                'Lettuce', 
                'Tomatoes',
                'Onion',
                'Avocado',
                'Cereals',
                'Ice+cream',
                'Cream+cheese', 
                'Tomato+sauce',
                'Spaghetti', 
                'Lasagna+noodles', 
                'Chocolate', 
              ]
def get_products(item):
    options = webdriver.SafariOptions()
    driver = webdriver.Safari(options=options)
    driver.get("https://www.walmart.com/search?q={0}".format(item))#
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source)

    prods = soup.find_all('span',class_="w_iUH7")
    products = []
    span_count=0
    for p_count , value in  enumerate(prods):
      
      if  item.lower() in value.text.lower() or 'price' in value.text :
        
        if 'price' in value.text:
          print('price')
          print(span_count)
          print(value.next)
          products[span_count].insert(1,value.text)#
          span_count +=1
        else:
          print('name')
          print(span_count)
          print(value.text)
          products.append([today]) 
          print(value.text)
          products[span_count].insert(0,value.text)
    driver.quit()
    print(products)
    return products



final_list = []
for item in grocery_list:
    final_list.extend( get_products(item))
   

list_of_tupples =[]
for items in  products:
    list_of_tupples.append(tuple(items))

print(final_list)

#insert_data(list_of_tupples)
