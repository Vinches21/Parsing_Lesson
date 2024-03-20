from random import choice
import requests

url = 'http://httpbin.org/ip'

with open('proxy.txt') as file:
    proxy_file = file.read().split('\n')
    for i in proxy_file:
        try:
            ip = i.strip()
            proxy = {
                'http': f'http://{ip}',
                'https': f'https://{ip}'
            }
            response = requests.get(url=url, proxies=proxy, timeout=5)
            print(response.json(), 'Success connection')
        except Exception as e:
            print(f"Ошибка при использовании прокси {proxy}: {e}")
            continue