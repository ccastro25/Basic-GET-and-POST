
from grocery_list import grocery_list
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pickle
import re
from datetime import  datetime

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
driver = webdriver.Chrome(options=options)
today = datetime.now().date() 


def get_product(item):
    driver.get("https://www.walmart.com/search?q={0}".format(item))
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source)
    titles = soup.find_all(attrs={"data-automation-id":"product-title"})
    prices =soup.find_all(attrs={"data-automation-id":"product-price"})
    products = []

    for i, v in enumerate(prices):
        price = prices[i]
        re.sub('[^0-9,.]','',price.find('span',class_='w_iUH7').text)
        value = re.sub('[^0-9,.]','',price.find('span',class_='w_iUH7').text)
        products.append((titles[i].text,value[len(value)-1],today,"Walmart"))
        if i==30:
          #Rabbery has issue when getting more than 36 products
          #Bacon
          break

    
    return products


def get_walmart_products():
    products = []
    for item in grocery_list:
        print("current item: {0}".format(item))
        products.extend( get_product(item))
        time.sleep(80)
  
    driver.quit()
    return products