
from grocery_list import grocery_list
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pickle
import re
from datetime import  datetime

 
today = datetime.now().date()


def get_product(item):
    driver = webdriver.Safari()
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