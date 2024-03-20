import requests

url = 'https://parsinger.ru/task/1/'
for n in range(1, 501):
    response = requests.get(url = f"https://parsinger.ru/task/1/{n}.html", timeout=1)
    if response.status_code == 200:
        print(n)
        break


