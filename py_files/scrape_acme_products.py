from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from datetime import  datetime
import pickle


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
today = datetime.now().date()

def get_products(item):
    driver = webdriver.Safari()

    driver.get("https://www.acmemarkets.com/shop/search-results.html?q={0}".format(item))
    print("this is the url: "+"https://www.acmemarkets.com/shop/search-results.html?q={0}".format(item) )
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source)
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
#save as pickle incase of error
with open('acme_products.pickle','wb') as f:
     pickle.dump(final_list,f)

#insert_data(final_list,"acmeproducts")