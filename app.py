from parse_page import parse_page
from selenium import webdriver

browser = webdriver.Firefox()
cnt = 1

while True:
    next_page = parse_page(
        f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{cnt}/c37l1700273',
        browser)
    if not next_page:
        break
    print(f'End of page {cnt}')
    cnt += 1

browser.close()
