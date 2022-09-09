import selenium
from sqlalchemy import insert
from database import ads_table, engine
from parse_block import *
from selenium.webdriver.common.by import By


def parse_page(link, browser):
    browser.get(link)

    ads = browser.find_elements(By.CSS_SELECTOR, value='div.search-item')
    try:
        pagination = browser.find_element(By.LINK_TEXT, value='Next >')
        isNextActive = True
    except selenium.common.exceptions.NoSuchElementException as e:
        isNextActive = False

    for ad in ads:
        stmt = (
            insert(ads_table).
            values(
                image=str(find_images(ad)),
                title=str(find_title(ad)),
                date=str(find_date(ad)),
                location=str(find_location(ad)),
                beds=str(number_of_beds(ad)),
                description=str(find_description(ad)),
                price=find_price(ad),
                currency='USD')
        )
        engine.execute(stmt)
    return isNextActive
