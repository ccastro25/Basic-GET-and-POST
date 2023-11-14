import requests
from bs4 import BeautifulSoup

ac="text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
target_url="https://www.walmart.com/search?q=Milk&affinityOverride=store_led&facet=fulfillment_method%3APickup"
headers={"Referer":"https://www.google.com","Connection":"Keep-Alive","Accept-Language":"en-US,en;q=0.9","Accept-Encoding":"gzip, deflate, br","Accept":ac,"User-Agent":"Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36 Safari/601.1"}

resp = requests.get(target_url, headers=headers)
print(resp.text)
url_search ="https://www.walmart.com/search?q=Milk&affinityOverride=store_led&facet=fulfillment_method%3APickup"
r = requests.get(url_search, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup)
s = soup.find_all("div", class_="  ")
#for loop to get all products
spans =s[0].find_all("span")
#product title under span with id product-title
title =spans[0].find_all("span")[0]
#price under div with product-price followed by 1st span. 2nd child div has fl oz
price = spans[0].find_all("span")[7]
image = spans[0].img