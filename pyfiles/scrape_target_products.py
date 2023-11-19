#https://www.target.com/s?searchTerm=milk&tref=typeahead%7Cterm%7Cmilk%7C%7C%7Chistory
#parent : span data-test= "current-price" child span
#a tag  data-test= "product-title"
from insert_data_to_mysql import insert_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from datetime import  datetime

   
today = datetime.now().date()

def get_products(item):


    driver = webdriver.Safari()
    #driver.get("https://www.walmart.com/search?q={0}".format(item))
    driver.get("https://www.target.com/s?searchTerm=milk")
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source)
    titles = soup.find_all(attrs={"data-test":"product-title"})
    prices =soup.find_all(attrs={"data-test":"current-price"})
    products = []
    for i, v in enumerate(titles):
        price = prices[i]
        value =price.find('span').text.split('$')
        products.append((titles[i].text,value[len(value)-1],today))
    print(products)
    driver.quit()
    return products