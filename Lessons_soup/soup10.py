import requests
from bs4 import BeautifulSoup


url = 'https://parsinger.ru/4.1/1/index5.html'

html = requests.get(url=url)
html.encoding = 'utf8'

soup  = BeautifulSoup(html.text, 'html.parser')


tag_email = soup.find_all('div', {"class":"email_field"})

sp = [email.find("strong").next_sibling.strip() for email in tag_email]
print(tag_email)