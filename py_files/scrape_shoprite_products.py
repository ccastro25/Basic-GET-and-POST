from insert_data_to_mysql import insert_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from datetime import  datetime
import re
import pickle

grocery_list =[ 'Raspberry',
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
                'Banana',
                'Frozen+pizza',
                'Grapes',
                'Strawberry',
                'Blueberry', 
               
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
today = datetime.now().date()

def get_products(item):
     driver = webdriver.Chrome()
     pattern = re.compile(r'^\d+-ProductNameTestId$')
     
     driver.get("https://www.shoprite.com/sm/pickup/rsid/3000/results?q={0}".format(item))
     time.sleep(2)
     soup = BeautifulSoup(driver.page_source)
     title = soup.find_all(attrs ={"data-testid":pattern})
     price = soup.find_all('div',class_="ProductPrice--w5mr9b")
     products =[]
     compare =''
     for i,v  in enumerate(title):
          if compare != title[i].text:
               products.append((title[i].text.split("Open")[0],price[i].text.replace('$', ''), today,"ShopRite"))
          compare = title[i].text

     driver.quit()
     print('this is a sample')
     print(products[3])
     return products

final_list = []
for item in grocery_list:
    print("current item: {0}".format(item))
    final_list.extend( get_products(item))
    print("starting")
    time.sleep(20)
    print("waiting 1 ") 
    time.sleep(20)
    print("waiting 2")
    time.sleep(20)
    print("waiting 3")
    time.sleep(20)
    print("done")
