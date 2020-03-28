# ReStudy_Compile.py
import re
regex = re.compile(r'[1-9]\d{5}')
rst = regex.search('BIT 100088 UXS100035')
print(type(rst))
if rst:
    print(rst.group(0))
    # match对象属性
    print(rst.string)   #待匹配的文本
    print(rst.re)       #匹配时使用的pattern对象(正则表达式)
    print(rst.pos)      #正则表达式搜索文本的开始位置
    print(rst.endpos)   #正则表达式搜索文本的结束位置
    print(rst.group(0)) #获得匹配后的字符串
    print(rst.start())  #匹配字符串在原始字符串的开始位置
    print(rst.end())    #匹配字符串在原始字符串的结束位置
    print(rst.span())   #返回(.start(),.end())  元组类型
match = re.search(r'PY.*?N', 'PYNANBNCNDN')
if match:
    print(match.group(0))