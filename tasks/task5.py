import requests

url = 'https://parsinger.ru/3.4/1/json_weather.json'
response = requests.get(url=url)
r = response.json()
res = 0
date = ''
for i in range(len(r)):
    elem = int((r[i]["Температура воздуха"]).replace('°C', ''))
    if elem <= res:
        res = elem
        date = r[i]['Дата']
print(date)