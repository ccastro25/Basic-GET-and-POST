
from insert_data_to_mysql import insert_data
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
    driver.get("https://www.walmart.com/search?q={0}".format(item))
    #driver.get("https://www.walmart.com/search?q=Rasberry")
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source)
    titles = soup.find_all(attrs={"data-automation-id":"product-title"})
    prices =soup.find_all(attrs={"data-automation-id":"product-price"})
    products = []

    for i, v in enumerate(titles):

        price = prices[i]
        value =price.find('span',class_='w_iUH7').text.split('$')
        products.append((titles[i].text,value[len(value)-1],today))
        if ==30:
          #Rabbery has issue when getting more than 36 products
          break
    print(products)
    driver.quit()
    return products


final_list = []
for item in grocery_list:
    print("current item: {0}".format(item))
    final_list.extend( get_products(item))
    print("starting")
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
