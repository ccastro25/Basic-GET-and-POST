from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from datetime import  datetime
import re
   
today = datetime.now().date()

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
def get_products(item):

pattern = re.compile(r'^\d+-ProductNameTestId$')
driver = webdriver.Safari()
driver.get("https://www.shoprite.com/sm/pickup/rsid/3000/results?q=milk")
soup = BeautifulSoup(driver.page_source)
title = soup.find_all(attrs ={"data-testid":pattern})
price = soup.find_all('div',class_="ProductPrice--w5mr9b")
for i,v  in enumerate(title):
     print(sp[i].text.split('Open')[0])

driver.quit()
return products