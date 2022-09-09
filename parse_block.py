from datetime import date, datetime
from selenium.webdriver.common.by import By


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def find_images(source):
    try:
        return source.find_element(By.CLASS_NAME, value='image'). \
            find_element(By.TAG_NAME, value='img').get_attribute('data-src')
    except:
        return 'No images provided'


def find_title(source):
    return source.find_element(By.CLASS_NAME, value='title').text


def find_date(source):
    date_of_post = source.find_element(By.CLASS_NAME, value='date-posted').text
    try:
        return datetime.strptime(date_of_post, "%d/%m/%Y").strftime("%d-%m-%Y")
    except:
        return date.today().strftime("%d-%m-%Y")


def find_location(source):
    try:
        return source.find_element(By.CLASS_NAME, value='location').find_element(By.TAG_NAME, value='span').text
    except:
        return 'No information provided'


def number_of_beds(source):
    try:
        return source.find_element(By.CLASS_NAME, value='bedrooms').text.replace('Beds: ', '')
    except:
        return 'No information provided'


def find_description(source):
    try:
        return source.find_element(By.CLASS_NAME, value='description').text
    except:
        return 'No information provided'


def find_price(source):
    price = source.find_element(By.CLASS_NAME, value='price').text
    if '$' in price:
        return price.replace('$', '')
    return price
