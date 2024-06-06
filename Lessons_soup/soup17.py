import requests
from bs4 import BeautifulSoup


# url = 'https://parsinger.ru/html/index1_page_1.html'
# base_url = 'https://parsinger.ru/html/'
# html = requests.get(url=url)
# html.encoding = "utf8"
# soup = BeautifulSoup(html.text, "html.parser")
#
# menu_pagen = [link["href"] for link in soup.find("div", class_="nav_menu").find_all("a")]
#
# for product in menu_pagen:
#     link_all = []
#     url_product = f"{base_url}{product}"
#     html = requests.get(url=url_product)
#     html.encoding = "utf8"
#     soup = BeautifulSoup(html.text, "html.parser")
#     pagen = [int(link.text) for link in soup.find("div", class_="pagen").find_all("a")][-1]
#     for link in range(1, pagen + 1):
#         url = f"https://parsinger.ru/html/"
#         link_all.append(f"https://parsinger.ru/html/{soup.find_all('a', class_='name_item').find()}")
#
#     print(pagen)


watch_url = 'https://parsinger.ru/html/index1_page_1.html'
html = requests.get(url=watch_url)
html.encoding = "utf8"
soup = BeautifulSoup(html.text, "html.parser")
pagen = [int(page.text) for page in soup.find("div", class_="pagen").find_all("a")][-1]

link_all = []
for i in range(1, 6):
    url = f"https://parsinger.ru/html/index{i}_page_1.html"
    for j in range(1, pagen+1):
        url = f"https://parsinger.ru/html/index{i}_page_{j}.html"
        html = requests.get(url=url)
        html.encoding = "utf8"
        soup = BeautifulSoup(html.text, "html.parser")
        link_watch = soup.find_all("a", class_="name_item")
        for x in link_watch:
            link_all.append(f"https://parsinger.ru/html/{x['href']}")

res = []
for product in link_all:
    url = product
    html = requests.get(url=url)
    html.encoding = "utf8"
    soup = BeautifulSoup(html.text, "html.parser")
    price = int(soup.select_one("#price").text.strip(" руб"))
    col = int(soup.select_one("#in_stock").text.strip("В наличии: "))
    res.append(price * col)




print(sum(res))