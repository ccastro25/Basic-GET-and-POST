from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import  datetime
from bs4 import BeautifulSoup
from grocery_list import grocery_list
import time
import pickle 
import re

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
driver = webdriver.Chrome(options=options)


today = datetime.now().date()

def get_product(item):
    driver.get(f"https://www.riteaid.com/shop/catalogsearch/result/?q={item}&Category=Food")    
    time.sleep(2)
                                
    soup = BeautifulSoup(driver.page_source,'html.parser')
    title =soup.find_all('div',class_='ra_prod_name')
    price  =soup.find_all('span',class_='ra_final-price')

    products =[]
    for i,v  in enumerate(title):
        products.append((title[i].text.strip(),price[i].text.replace('$', ''), today,"Rite-Aid"))

    return products

def get_riteaid_products():
    products = []
    for item in grocery_list:
        print(f"current item: {item}")
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



