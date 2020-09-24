import requests
from bs4 import BeautifulSoup

# URL = 'https://www.amazon.in/HP-Pavilion-14-CE1073TX-i5-8265U-Graphics/dp/B07TC65VBS/ref=sr_1_2_sspa?dchild=1&keywords=laptop&qid=1600976533&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSjc5SjBGMzZER1laJmVuY3J5cHRlZElkPUEwNTk1MDM5N0pWRzRUS0FYNUdNJmVuY3J5cHRlZEFkSWQ9QTAzMDcyMzEzVEs1WTFUQ0tWS0xQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
URL = 'https://www.amazon.in/Apple-iPhone-11-64GB-Black/dp/B07XVMDRZY/ref=sr_1_1?dchild=1&keywords=iphone&qid=1600977029&sr=8-1'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# price = soup.find(id='priceblock_dealprice')

# print(price)

# product_price = soup.find_all('span', {'class': ['a-size-medium a-color-price priceBlockDealPriceString']})
product_price = soup.find_all('span', {'class': ['a-size-medium a-color-price priceBlockBuyingPriceString']})

# print(soup.prettify())
print(product_price)
