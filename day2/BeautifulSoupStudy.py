# BeautifulSoupStudy.py
from bs4 import BeautifulSoup
# 演示HTML页面地址：http://python123.io/ws/demo.html
# import requests
# r = requests.get('http://python123.io/ws/demo.html')
# demo = r.text
demo = open('demo.html', 'r')
soup = BeautifulSoup(demo, "html.parser")
# print(soup.prettify())    #输出整个页面
print(soup.title)           #页面标题
tag = soup.a                #找到第一个a标签
print(tag)                  #输出标签
print(soup.a.string)        #第一个a标签的字符串
print(soup.a.parent.name)   #a标签的父类的名字
print(soup.a.parent.parent.name)#a标签的父类的父类的名字
print(tag.attrs)            #获取a标签的全部属性(字典类型)
print(tag.attrs['class'])   #获取a标签的指定属性
print(tag.attrs['id'])
print(type(tag.attrs))      #标签属性的类型(字典'dict')
print(type(tag))            #标签的类型(bs库自定义属性'bs4.element.Tag')
# 标签字符串的类型(bs库自定义属性'bs4.element.NavigableString')
print(type(soup.p.string))  #NavigableString可以跨越多个标签层次
print(soup.b)               #b标签内容被注释
print(type(soup.b.string))  #查看被注释字符串的类型('bs4.element.Comment')
demo.close()    #关闭文件读取