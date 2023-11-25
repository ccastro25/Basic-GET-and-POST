from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import  datetime
from bs4 import BeautifulSoup
from collect_and_save_products import get_save_items
import time 


today = datetime.now().date()

def get_acme_products(item):
    driver = webdriver.Safari()

    driver.get(f"https://www.acmemarkets.com/shop/search-results.html?q={item}")
    print(f"this is the url: "+"https://www.acmemarkets.com/shop/search-results.html?q={item}" )
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    title = soup.find_all('a',attrs={'data-qa': 'prd-itm-pttl'})
    #price retrieves all values  
    price = soup.find_all('span',attrs={'data-qa':'prd-itm-prc'})

    products =[]

    for i,v  in enumerate(title):
            products.append((title[i].text,price[i].text.split(' ')[2].replace('$', ''), today,"ACME"))
        

    driver.quit()
    print('this is a sample')
    print(products)
    return products

get_save_items('acme_products',get_acme_products)