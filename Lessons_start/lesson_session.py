import requests

# Создание объекта сессии
session = requests.Session()

# Установка заголовков для сессии
session.headers.update({'User-Agent': 'my_parser'})

# Отправка запроса через объект сессии
response = session.get('https://example.com')

# Доступ к тексту ответа
print(session.headers['User-Agent'])

# Код с сессией

import time

# Создание объекта сессии
session2 = requests.Session()

# Измерение времени выполнения запросов с переиспользованием соединения
start_time = time.time()
for _ in range(10):
    response = session2.get('https://example.com')
end_time = time.time()

print(f'Время выполнения с переиспользованием соединения: {end_time - start_time}')

#Настройка прокси для сессии

proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}

session3 = requests.Session()
session3.proxies.update(proxies)

response = session3.get('http://example.org')