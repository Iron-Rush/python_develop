# KeyWordMixSearch.py
# 引入正则表达式库
import re
from bs4 import BeautifulSoup
demo = open('demo.html', 'r')
soup = BeautifulSoup(demo, "html.parser")
for link in soup.find_all(['a', 'b']):
    # print(link.get('href'))
    print(link)
print('打印全部标签名称')
for tag in soup.findAll(True):
    print(tag.name)
#
print('打印包含b的标签')
for tag in soup.find_all(re.compile('b')):
    print(tag.name)
# 打印带'course属性的p标签
print(soup.find_all('p', 'course'))
# 打印属性中id=link1的标签
print(soup.find_all(id='link1'))
# 检索字符串为Basic Python
print(soup.find_all(recursive= False, string= 'Basic Python'))
# 检索字符串包含Python
print(soup.find_all(string= re.compile('Python')))
demo.close()