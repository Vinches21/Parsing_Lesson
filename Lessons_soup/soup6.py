import requests
from bs4 import BeautifulSoup

html_res = requests.get(url = "https://parsinger.ru/4.3/4/index.html")
html_res.encoding = "utf8"

soup = BeautifulSoup(html_res.text, "html.parser")

result = soup.find_all("p")
print(result)
# for tag in result:
#     print(type(tag["id"]))
total_id_sum = 0
total_class_sum = 0

# for tag in result:
#     print(tag["class"])

for tag in result:
    if len(tag.string.replace(" ", "")) % 2 == 0:
        total_id_sum += int(tag["id"])
        total_class_sum += int(tag["class"][0])



print(total_id_sum + total_class_sum)

