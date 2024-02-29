import requests

"""Задача по скачиванию 160 картинок и нахоэдения кода на одной из них - 3.4"""


"""Мой код"""
for i in range(1, 161):
    url = fr'https://parsinger.ru/img_download/img/ready/{i}.png'
    response = requests.get(url=url)
    with open(fr'../content/image{i}.png', 'wb') as file:
        file.write(response.content)


"""Альтернативный вариант"""
# url = 'http://parsinger.ru/img_download/'
# resp = requests.get(url)
# soup = bs(resp.text, 'html.parser')
#
# for link in tqdm(soup.findAll('img')):
#     img_url = link.get('src')
#     img = Image.open(BytesIO(requests.get(f'{url}{img_url}').content))
#     if img.histogram()[0] != 0:
#         img.save('img_with_answer.png')
#         break