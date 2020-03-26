# BeautifulSoupComment.py
from bs4 import BeautifulSoup
soup = BeautifulSoup("<b><!--This is a comment--></b>"
                     "<p>This is not a comment</p>", "html.parser")
print(soup.b.string)
print(type(soup.b.string))  # 被注释的b标签字符串的类型(<class 'bs4.element.Comment'>)

print(soup.p.string)
print(type(soup.p.string))  # 未被注释的p标签字符串的类型(<class 'bs4.element.Comment'>)
