import requests
from bs4 import BeautifulSoup

def formula(new_price, old_price):
    f = ((old_price - new_price) * 100 / old_price)
    print(round(f, 1))


url = 'https://parsinger.ru/html/hdd/4/4_1.html'

html = requests.get(url=url)
soup = BeautifulSoup(html.text, "html.parser")

old = int(soup.find("span", id="old_price").text.strip(" руб"))
new = int(soup.find("span", id="price").text.strip(" руб"))


formula(new_price=new, old_price=old)