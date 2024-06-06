import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/1/index.html'

response = requests.get(url=url)

response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')

headers = [header.text for header in table.find_all("th")]
rows = table.find_all("tr")[1:]
res = []

for row in rows:
    column = row.find_all("td")
    for col in column:
        res.append(float(col.text))
print(sum(set(res)))
    # res.append(int(row.find_all("td").text))



# print(sum(res))