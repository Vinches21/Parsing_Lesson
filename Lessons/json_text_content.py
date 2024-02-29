from pprint import pprint

import requests

# Отправляем GET-запрос
# r = requests.get('https://api.github.com/events')

# Узнать текущую кодировку
# print("Текущая кодировка:", r.encoding)

# Изменить кодировку
# r.encoding = 'ISO-8859-1'
# print(r.encoding)

# r = requests.get(url='https://jsonplaceholder.typicode.com/todos/')
# pprint(r.json())

# Проверка статуса ответа
# if r.status_code == 200:
#     print("Запрос успешно выполнен")
# else:
#     print(f"Произошла ошибка: {r.status_code}")

"""Сохранение контента в файл"""
response = requests.get(url='http://httpbin.org/image/jpeg')
with open('../content/image.jpeg', 'wb') as file:
    file.write(response.content)