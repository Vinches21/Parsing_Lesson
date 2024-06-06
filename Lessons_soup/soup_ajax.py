import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'cf_clearance': "Uf0YD1Q1a7WAbbKOjurx2F0ZNQSYxTSaw72oZusLtPM",
    "Accept": "application/json"
}

# data = {
#     "GiveName": "Monero",
#     "GetName": "Dash",
#     "Sum": 100,
#     "Direction": 0
# }

url = "https://bitality.cc/Home/GetSum?GiveName=PancakeSwap&GetName=VeChain&Sum=41.14383838&Direction=0"
response = requests.get(url=url, headers=headers)
if 'application/json' in response.headers['Content-Type']:

    data = response.json()
    print(data)
else:
    print('Ответ не в формате JSON')
print(f"Content-Type: {response.headers['Content-Type']}")

# import requests
# from bs4 import BeautifulSoup
# from random import choice
#
# url = "https://bitality.cc"
# response = requests.get(url)
# response.encoding = 'utf-8'
#
# soup = BeautifulSoup(response.text, 'lxml')
#
# available_currencies = sorted(list(set([el.text for el in  soup.find_all('span', class_='ml-2 b-choose__item-txt')])))
#
# qt = input('Введите количество валюты для обмена: ')
#
# data = {
#     'GiveName': choice(available_currencies),
#     'GetName': choice(available_currencies),
#     'Sum': qt,
#     'Direction': 0
# }
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
#     'x-requested-with': 'XMLHttpRequest'
# }
# work_url = 'https://bitality.cc/Home/GetSum'
#
# response = requests.get(url = work_url, headers=headers, params=data).json()
#
# print(f"Если дашь {qt} {data['GiveName']}, получишь {response['getSum']} {data['GetName']}")