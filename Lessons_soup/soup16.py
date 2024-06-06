import requests
from bs4 import BeautifulSoup


summa = []
for i in range(1, 33):
    url = f"https://parsinger.ru/html/mouse/3/3_{i}.html"
    html = requests.get(url=url)
    html.encoding = "utf8"
    soup = BeautifulSoup(html.text, 'html.parser')
    summa.append(int(soup.select_one(".article").text.strip("Артикул: ")))


print(sum(summa))