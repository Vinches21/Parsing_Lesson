import requests
from bs4 import BeautifulSoup


url = 'https://parsinger.ru/4.1/1/index4.html'

html = requests.get(url=url)
html.encoding = 'utf8'

soup  = BeautifulSoup(html.text, 'html.parser')



# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     prices = soup.find_all("p", class_="price product_price")
#
#     count = 0
#     for price in prices:
#         # Допишите обработку тегов и суммирование цен
#         count+= int(price.text.strip(' руб'))
#
#     return count
#
# print(get_html(html))

# soup = BeautifulSoup(html.text, 'html.parser')
#
# prices = soup.find_all("p", class_="price product_price")
# for price in prices:
#     print(int(price.text.replace(" руб", "").replace(" ", '')))
# print(prices)

soup = BeautifulSoup(html.text, 'html.parser')

# prices = soup.find_all("li", id=True)
prices = soup.select("li")

for i in prices:
    print(i["id"])

print(len(prices))