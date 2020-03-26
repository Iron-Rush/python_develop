# BeautifulSoupPrettify.py
from bs4 import BeautifulSoup
import requests
r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
# demo = open('demo.html', 'r')
# soup = BeautifulSoup(demo, "html.parser")
soup = BeautifulSoup(demo, "html.parser")
print(demo)
print(soup.prettify())  #格式化换行输出页面