import requests



url='https://scrapingclub.com/exercise/ajaxdetail_header/'

response = requests.get(url=url)
if 'application/json' in response.headers['Content-Type']:

    data = response.json()
    print(data)
else:
    print('Ответ не в формате JSON')
print(f"Content-Type: {response.headers['Content-Type']}")