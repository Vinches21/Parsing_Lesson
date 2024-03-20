import requests
from bs4 import BeautifulSoup

# Базовый URL для поиска в онлайн-магазине
base_url = 'https://example.com/search'

# Параметры поиска: ищем ноутбуки с определенными характеристиками
search_params = {
    'query': 'note',  # Поисковый запрос
    'brand': 'Dell',  # Бренд
    'min_price': '50000',  # Минимальная цена
    'max_price': '100000',  # Максимальная цена
    'sort': 'price_asc'  # Сортировка по возрастанию цены
}

# Отправляем GET-запрос с параметрами
response = requests.get(base_url, params=search_params)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсим HTML-страницу с использованием BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все элементы, соответствующие карточкам товаров (здесь это примерный CSS-селектор)
    product_cards = soup.select('.product-card')

    for card in product_cards:
        # Извлекаем информацию из карточки товара (название и цена)
        product_name = card.select_one('.product-name').text
        product_price = card.select_one('.product-price').text

        print(f'Название товара: {product_name}')
        print(f'Цена товара: {product_price}')
        print('---')
else:
    print(f'Не удалось выполнить запрос. Код ошибки: {response.status_code}')
    print(response.url)