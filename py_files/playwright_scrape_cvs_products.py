import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


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
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)