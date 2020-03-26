# BeautifulSoupTraverseUp.py
from bs4 import BeautifulSoup
demo = open('demo.html', 'r')
soup = BeautifulSoup(demo, "html.parser")
# 遍历全部先辈标签时，会遍历到soup本身，soup先辈不存在.name信息
# 因此如果parent不存在，则不打印parent.name
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)