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
today = datetime.now().date()



products = {}

for p_count , value in  enumerate(prods):
    span = value.find_all('span',class_="w_iUH7")
    if len(span)>1: 
     d[p_count] =[]    
     for count , value in  enumerate(span):
        d[p_count].append(value.text)
 