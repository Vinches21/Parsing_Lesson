from bs4 import BeautifulSoup

html = "<div class='myclass'>Hello, world!</div>"
soup = BeautifulSoup(html, 'html.parser')

tag = soup.div

print(type(tag))   # <class 'bs4.element.Tag'>
print(tag.name)    # div
print(tag.attrs)   # {'class': ['myclass']}
print(tag.string)  # Hello, world!