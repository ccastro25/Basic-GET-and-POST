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
#driver.get("https://www.target.com/s?searchTerm={0}".format(item))
driver.get("https://www.target.com/s?searchTerm=milk")
time.sleep(2)
soup = BeautifulSoup(driver.page_source,'html.parser')
#attrs does not seem to work , prices do not seem to appear , 
titles = soup.find_all(attrs={"data-test":"product-title"})
prices =soup.find_all(attrs={"data-test":"current-price"})
products = []
a =soup.find_all('a')
for i, v in enumerate(titles):
    price = prices[i]
    value =price.find('span').text.split('$')
    products.append((titles[i].text,value[len(value)-1],today))
print(products)
driver.quit()
return products



#possible option to get title
class="styles__PriceStandardLineHeight-sc-b5yooy-0 kKRufV"
des = soup.find_all(class_='styles__StyledLink-sc-vpsldm-0 eqjfDm')
class="styles__ProductCardPriceAndPromoStyled-sc-j7z9dv-0 bQvAZT"

#subcription based target api . 15 a month for hobbiest
import requests
import json

# set up the request parameters
params = {
  'api_key': 'demo',
  'type': 'search',
  'search_term': 'milk'
}

# make the http GET request to RedCircle API
api_result = requests.get('https://api.redcircleapi.com/request', params)

# print the JSON response from RedCircle API
print(json.dumps(api_result.json()))