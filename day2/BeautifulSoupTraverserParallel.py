# BeautifulSoupTraverserParallel.py
from bs4 import BeautifulSoup
demo = open('demo.html', 'r')
soup = BeautifulSoup(demo, "html.parser")
print(soup.a.next_sibling.next_sibling) #a标签的下下个平行节点
print(soup.a.previous_sibling)          #a标签的前一个平行节点
for sibling in soup.a.next_siblings:    #遍历后续全部平行节点
    print(sibling)