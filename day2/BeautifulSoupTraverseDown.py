# BeautifulSoupTraverseDown.py
from bs4 import BeautifulSoup
demo = open('demo.html', 'r')
soup = BeautifulSoup(demo, "html.parser")
print(soup.head)
print(soup.head.contents)
print(soup.body.contents)
print(len(soup.body.contents))  #body标签下面有5个节点
print(soup.body.contents[1])
i = 0
# 。contents(列表，可通过下标获取)
# .children(迭代器，所有儿子节点)
# .descendants(迭代器，后续全部子孙节点)
for child in soup.body.descendants:
    # print(child)
    i += 1
print(i)