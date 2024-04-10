import requests
from bs4 import BeautifulSoup




# url = 'https://parsinger.ru/4.1/1/index3.html'
# html_res = requests.get(url=url)
# html_res.encoding = 'utf8'

# soup = BeautifulSoup(html_res.text, 'html.parser')
# print(soup)
# tag = soup.find(attrs={"data-gpu":"nVidia GeForce RTX 4060"})
# print(tag.text)

# url = 'https://parsinger.ru/4.1/1/index.html'
# html_res = requests.get(url=url)
# html_res.encoding = 'utf8'
# soup = BeautifulSoup(html_res.text, 'html.parser')
# print(soup)
# a = soup.find("a")
# img = a.find("img", )
# print("_______")
# print(img)

# soup = BeautifulSoup(html_res.text, 'html.parser')
#
# li_tag = soup.find(class_ = "description detailz")
#
# print(li_tag.text)

url = 'https://parsinger.ru/4.1/1/index2.html'
html_res = requests.get(url=url)
html_res.encoding = 'utf8'

soup = BeautifulSoup(html_res.text, 'html.parser')
tag = soup.find("div").find("li", attrs={
    "class":["description_detail", "class1", "class2", "class3"],
    "data-fdg45":"value13",
    "data-54dfg60":"value14",
    "data-d6f50hg":"value15"

})

print(tag.text)