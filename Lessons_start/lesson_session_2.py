import requests
from itertools import cycle

# Список прокси
proxies_list = [
    {'http': 'http://10.10.36.159:8000', 'https': 'https://10.10.36.159:8000'},
    {'http': 'http://10.10.51.205:8000', 'https': 'https://10.10.51.205:8000'},
    {'http': 'http://10.10.79.216:8000', 'https': 'https://10.10.79.216:8000'},
    # ... и так далее
]

proxy_pool = cycle(proxies_list)

url = "http://example.org"

# Создание сессии
session = requests.Session()

for i in range(1, 6):  # Попробуем сделать 5 запросов
    proxy = next(proxy_pool)
    session.proxies.update(proxy)  # Обновление прокси для сессии
    try:
        response = session.get(url, timeout=5)  # Используем сессию для выполнения запроса
        print(f"Request {i}: Success!")
    except requests.exceptions.RequestException as e:
        print(f"Request {i}: Failed, switching proxy. {proxy}")

#Аутентификация на прокси

url = "https://httpbin.org/ip"
proxies = {
    'http': 'socks5://8ZYk5H:XfMpg7@10.10.36.159:8000',
    'https': 'socks5://Kx4Jcj:h4Ch0N@10.10.51.205:8000',
}

# Создаем сессию
session2 = requests.Session()

# Устанавливаем прокси для сессии
session2.proxies.update(proxies)

# Делаем запрос
response = session2.get(url)

print(response.text)