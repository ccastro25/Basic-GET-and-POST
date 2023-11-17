rom selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from insert_data_to_mysql import insert_data
from datetime import  datetime
   
today = datetime.now().date()
browser = webdriver.Safari()
grocery_list =[
                'Eggs',
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
    browser.get("https://www.walmart.com/search?q=milk&affinityOverride=store_led&facet=fulfillment_method%3APickup")#.format(item
    soup = BeautifulSoup(browser.page_source)
    #just use soup.find_all('span',class_='w_iUH7') , just get spans. but will have to refactor loops 
    prods = soup.find_all('span',class_="w_iUH7")
    print(item)
    products = []
    span_count=0
    for p_count , value in  enumerate(prods):
        if p_count >1 and not 'reviews' in value.text:
          print(value.text) 
          if 'price' in value.text:
            products[span_count].insert(1,value.text.split("price $")[1])
            span_count +=1
          else:
            print(span_count)
            products.append([today])
            products[span_count].insert(0,value.text)


final_list = []
for item in grocery_list:
    final_list.extend( get_products(item))

list_of_tupples =[]
for items in  products:
    list_of_tupples.append(tuple(items))

insert_data(list_of_tupples)