import  requests





for i in range(1, 101):
    url = f"https://parsinger.ru/3.3/4/{i}.html"
    response = requests.get(url=url, timeout=5)
    if response.status_code == 200:
        print(f"Первая доступная страница: {i}.html")