import selenium

from parse_block import *
from selenium.webdriver.common.by import By


def parse_page(link, browser):
    browser.get(link)
    list_of_items = []

    ads = browser.find_elements(By.CSS_SELECTOR, value='div.search-item')
    try:
        pagination = browser.find_element(By.LINK_TEXT, value='Next >')
        isNextActive = True
    except selenium.common.exceptions.NoSuchElementException as e:
        isNextActive = False

    for ad in ads:
        ad_data = [
            find_images(ad),
            find_title(ad),
            find_date(ad),
            find_location(ad),
            number_of_beds(ad),
            find_description(ad),
            find_price(ad)
        ]
        list_of_items.append(ad_data)
    return list_of_items, isNextActive
