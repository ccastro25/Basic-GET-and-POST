from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import  datetime
from bs4 import BeautifulSoup
from collect_and_save_products import get_save_items
from grocery_list import grocery_list
import time 


options = webdriver.SafariOptions()
#options.add_argument('--headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
driver = webdriver.Safari(options=options)
driver.get(f"https://www.riteaid.com/")

today = datetime.now().date()

def get_acme_products(item):
       
time.sleep(2)
inpu = driver.find_element(By.CLASS_NAME, "cx-header-menu__search-textbox")

inpu.clear()
inpu.send_keys(item)
time.sleep(2)
inpu.send_keys(Keys.RETURN)
time.sleep(5)
inpu = driver.find_element(By.CLASS_NAME,"myCheckbox_43617465676f727920466f6f64")
inpu.click()
soup = BeautifulSoup(driver.page_source,'html.parser')
title =soup.find_all('div',class_='ra_prod_name')
price  =soup.find_all('span',class_='ra_final-price')


products =[]
for i,v  in enumerate(title):
    products.append((title[i].text,price[i].text.split(' ')[2].replace('$', ''), today,"ACME"))

print('this is a sample')
print(products)
return products


products = []
for item in grocery_list:
    print(f"current item: {item}")
    products.extend( get_acme_products(item))
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

with open('rite_aid.pickle','wb') as f:
    pickle.dump(final_list,f) 
insert_data(final_list,store_product)

#get_save_items('acme_products',get_acme_products)

