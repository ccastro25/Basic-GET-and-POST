from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from insert_data_to_mysql import insert_data
from datetime import  datetime
   
today = datetime.now().date()
browser = webdriver.Safari()
browser.get("https://www.walmart.com/search?q=Milk&affinityOverride=store_led&facet=fulfillment_method%3APickup")

soup = BeautifulSoup(browser.page_source)
prods = soup.find_all("div",class_='mb0')

products = []
span_count=0
for p_count , value in  enumerate(prods):
    span = value.find_all('span',class_="w_iUH7")
    if len(span)>1:
      products.append([today]) 
      p_len = len(products)-1
      for count , value in  enumerate(span):
        if count <=1:
            if count==1:
              products[p_len].insert(count,value.text.split("price $")[1])
            else:
                 products[p_len].insert(count,value.text)

seq_of_params =[]
for items in  products:
    seq_of_params.append(tuple(items))
print(seq_of_params)
#insert_data(seq_of_params)