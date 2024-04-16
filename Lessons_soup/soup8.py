import requests
from bs4 import BeautifulSoup


url = 'https://parsinger.ru/4.1/1/index4.html'

html = requests.get(url=url)
html.encoding = 'utf8'

soup  = BeautifulSoup(html.text, 'html.parser')


# tags = soup.find_all("div", attrs={"class": "img_box product_img_box"})
# tags = soup.select('div[class="img_box product_img_box"] [class="name_item product_name"]')
#
# print(tags)
# for tag in tags:
#     print(tag.text.strip())  # Извлеките текст и обрежьте лишние пробелы

tags = soup.find_all('a', class_ = 'name_item')
for tag in tags:
    print(tag.text.strip())