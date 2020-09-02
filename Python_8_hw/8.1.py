import requests
from bs4 import BeautifulSoup
import dataset

url = 'https://mymotoshop.ru/held-motokurtka/'

resp = requests.get(url)
print(resp.text)

soup = BeautifulSoup(resp.text)

group_selector = "#res-produсts > div.product-grid.row > div:nth-chils(1)"

groups = soup.select(group_selector)

# print(groups)


def get_price(s):
    s = s.replace(" ", "")
    dot_index = s.find(".")
    if dot_index > 0:
        s = s[:dot_index]
    return s


for group in groups:
    try:
        name = groups.select_one(".name").get_text().strip()
        print(name)

        price_str = group.select_one(".price").get_text()
        price = get_price(price_str)
        print(price)

        product_url = group.select_one(".name a"['href'])
        print(product_url)


    except Exception as exc:
        print(exc)
        continue