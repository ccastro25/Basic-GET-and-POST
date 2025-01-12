import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from grocery_list import grocery_list
from datetime import  datetime
from bs4 import BeautifulSoup
import pickle  

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cvs.com/")
    page.click('#changeStore')
    page.get_by_role("textbox", name="Search by Zip Code, City,").click()
    time.sleep(2)
   # page.locator("#store-search-box").fill("19124").press("Enter")
    page.get_by_role("textbox", name="Search by Zip Code, City,").fill("19124")
    time.sleep(2)
    page.get_by_role("textbox", name="Search by Zip Code, City,").press("Enter")
    page.get_by_role("banner").locator("#submit").click()
    #page.get_by_role("button", name="Select store at 4133 G ST.").click()
    first_button = page.query_selector('#storeSelected') 
    first_button.click()
    time.sleep(2)
    page.get_by_role("dialog", name="Change your CVS Store").get_by_label("Close").click()
    page.get_by_role("combobox", name="Search products and services").click()
    time.sleep(2)
    page.get_by_role("option", name="Search for colgate").click()
    
    # ---------------------
    #page.waitForNavigation(waitUntil="networkidle") 
    page.wait_for_url(page.url)
    html = page.content()
    soup = BeautifulSoup(html,'html.parser')
    price =soup.find_all('div',class_="css-901oao r-1xaesmv r-ubezar r-majxgm r-wk8lta")
    title =soup.find_all('div',class_="css-901oao css-cens5h r-b0vftf r-1xaesmv r-ubezar r-majxgm r-29m4ib r-rjixqe r-1mnahxq r-fdjqy7 r-13qz1uu")

    products =[]
    for i,v  in enumerate(title):
        products.append((title[i].text, re.sub('[^0-9,.]','',price[i].text), today, "CVS"))
      
 

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

from playwright.sync_api import sync_playwright
'''
    thiss popup comes up at times
def handle_popup(page):
    try:
        # Check if the popup is present
        if page.query_selector('.kpl-invitation-content.sc-jTzLTM.dcUJFw'):
            page.click('#kplDeferButton')
            print("Popup closed.")
    except Exception as e:
        print(f"No popup found: {e}")
'''

