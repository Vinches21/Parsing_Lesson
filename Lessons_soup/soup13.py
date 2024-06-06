import requests
from bs4 import BeautifulSoup


url = 'https://parsinger.ru/html/index1_page_1.html'

html = requests.get(url=url)
html.encoding = 'utf8'

soup = BeautifulSoup(html.text, "html.parser")

# tag_price = soup.find_all("p", class_="price")
tag_price = soup.select("p.price")

res = sum([int(tag.text.replace(" руб", '')) for tag in tag_price])
print(res)