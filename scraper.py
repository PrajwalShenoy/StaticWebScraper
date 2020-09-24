import requests
from bs4 import BeautifulSoup

URL = 'https://webscraper.io/test-sites/e-commerce/allinone'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

product_price = soup.find_all('h4', {'class': ['pull-right price']})

# print(soup.prettify())
for i in product_price:
    print(i.prettify())
    