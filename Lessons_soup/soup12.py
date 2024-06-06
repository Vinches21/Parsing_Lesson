import requests
from bs4 import BeautifulSoup


url = 'https://parsinger.ru/html/index1_page_1.html'

html = requests.get(url=url)
html.encoding = 'utf8'

soup  = BeautifulSoup(html.text, 'html.parser')

tags = soup.find_all("p", class_="price")

print(*(tag.text.strip(" руб") for tag in tags), sep = '\n')