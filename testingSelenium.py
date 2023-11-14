from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

browser = webdriver.Safari()
browser.get("https://www.walmart.com/search?q=Milk&affinityOverride=store_led&facet=fulfillment_method%3APickup")

soup = BeautifulSoup(browser.page_source)
prods = soup.find_all("div",class_='mb0')

for i in range(len(prods)):
    span = prods[i].find_all('span')
    price = span[8].text.split("price ")[1]
    title = span[0].text
    #call db and insert values 


