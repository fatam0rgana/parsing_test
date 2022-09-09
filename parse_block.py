from datetime import date, datetime
from selenium.webdriver.common.by import By


def find_images(source):
    return source.find_element(By.CLASS_NAME, value='image'). \
        find_element(By.TAG_NAME, value='img').get_attribute('data-src')


def find_title(source):
    return source.find_element(By.CLASS_NAME, value='title').text


def find_date(source):
    date_of_post = source.find_element(By.CLASS_NAME, value='date-posted').text
    try:
        return datetime.strptime(date_of_post, "%d/%m/%Y").strftime("%d-%m-%Y")
    except:
        return date.today().strftime("%d-%m-%Y")


def find_location(source):
    return source.find_element(By.CLASS_NAME, value='location').find_element(By.TAG_NAME, value='span').text


def number_of_beds(source):
    return source.find_element(By.CLASS_NAME, value='bedrooms').text


def find_description(source):
    return source.find_element(By.CLASS_NAME, value='description').text


def find_price(source):
    return source.find_element(By.CLASS_NAME, value='price').text
