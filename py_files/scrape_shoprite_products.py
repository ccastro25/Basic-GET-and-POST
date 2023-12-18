from grocery_list import grocery_list
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from datetime import  datetime
import re
import pickle

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
driver = webdriver.Chrome(options=options)
today = datetime.now().date()

def get_product(item):
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
          time.sleep(80)
     driver.quit()
     return products