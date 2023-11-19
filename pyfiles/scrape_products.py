
from insert_data_to_mysql import insert_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from datetime import  datetime
import geocoder
   
today = datetime.now().date()

grocery_list =[
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
                'Platano',
                'Frozen+pizza'
                'Grapes',
                'Strawberry',
                'Blueberry', 
                'Raspberry',
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

    lat_and_lon = geocoder.ip('me')
    store_location = lat_and_lon.json['city']+' Store'
    driver = webdriver.Safari()
    driver.get("https://www.walmart.com/search?q={0}".format(item))
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source)
    titles = soup.find_all(attrs={"data-automation-id":"product-title"})
    prices =soup.find_all(attrs={"data-automation-id":"product-price"})
    products = []
    for i, v in enumerate(titles):
        price = prices[i]
        value =price.find('span',class_='w_iUH7').text.split('$')
        products.append((titles[i].text,value[len(value)-1],today))
    driver.quit()
    return products


final_list = []
for item in grocery_list:
    print("current item: {0}".format(item))
    final_list.extend( get_products(item))
    #may 120
    time.sleep(20)
    print("waiting 1 ") 
    time.sleep(20)
    print("waiting 2")
    time.sleep(20)
    print("waiting 3")
    time.sleep(20)
    print("done")

print(final_list)

insert_data(list_of_tupples)
