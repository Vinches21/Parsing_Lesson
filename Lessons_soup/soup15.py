import requests
from bs4 import BeautifulSoup


url = 'https://parsinger.ru/html/index3_page_1.html'

base_url = 'https://parsinger.ru/html/'

html = requests.get(url=url)
html.encoding = "utf8"
soup = BeautifulSoup(html.text, "html.parser")

pagen = [f"{base_url}{link['href']}" for link in soup.find("div", class_ = "pagen").find_all("a")]

res = []
for product in pagen:
    s = requests.get(url=product)
    s.encoding = "utf8"
    soup_page = BeautifulSoup(s.text, "html.parser")
    a = [pr.text for pr in soup_page.select(".img_box .name_item")]
    res.append([pr.text for pr in soup_page.select(".img_box .name_item")])
print(res)