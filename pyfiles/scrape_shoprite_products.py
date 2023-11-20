'''data-testid="00093966009989-ProductNameTestId"
data-testid="00742365264351-ProductNameTestId"
data-testid="productCardPricing-div-testId"
'''
class="ProductCardNameWrapper--g2y3vm boGWcY"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from datetime import  datetime

   
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


driver = webdriver.Safari()
driver.get("https://www.shoprite.com/sm/pickup/rsid/3000/results?q=milk")

soup = BeautifulSoup(driver.page_source)
title = soup.find_all('div',class_="ProductCardNameWrapper--g2y3vm boGWcY")
price =soup.find_all('div',attrs={'data-testid':"productCardPricing-div-testId"})
for p in price:
     print(p.text)
products = []

driver.quit()
return products