from grocery_list import grocery_list
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from datetime import  datetime
import re
import pickle

today = datetime.now().date()

def get_product(item):
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
               products.append((title[i].text.split("Open")[0],re.sub('[^0-9,.]','',price[i].text), today,"ShopRite"))
          compare = title[i].text

     return products

def get_shoprite_products():
     products = []
     for item in grocery_list:
          print("current item: {0}".format(item))
          products.extend( get_product(item))
          print("starting")
          time.sleep(20)
          print("waiting 1 ") 
          time.sleep(20)
          print("waiting 2")
          time.sleep(20)
          print("waiting 3")
          time.sleep(20)
          print("done")
     driver.quit()
     return products