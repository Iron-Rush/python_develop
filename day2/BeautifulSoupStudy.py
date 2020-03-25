# BeautifulSoupStudy.py
from bs4 import BeautifulSoup
# 演示HTML页面地址：http://python123.io/ws/demo.html
import requests
r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())