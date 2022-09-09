from parse_page import parse_page
from selenium import webdriver

browser = webdriver.Firefox()
cnt = 100

for i in range(2):
    items, next_page = parse_page(
        f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{cnt}/c37l1700273?sort=dateAsc',
        browser)
    print(items)
    if not next_page:
        break
    cnt += 1

browser.close()
