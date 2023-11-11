import requests
from bs4 import BeautifulSoup
def scrap():
    keyword = "milk"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
     url_search ="https://www.walmart.com/search?q=milk"
    r = requests.get(url_search, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find_all("div", class_="  ")
    #for loop to get all products
    spans =s[0].find_all("span")
    #product title under span with id product-title
    title =spans[0].find_all("span")[0]
    #price under div with product-price followed by 1st span. 2nd child div has fl oz
    price = spans[0].find_all("span")[7]
    image = spans[0].img