# ReStudy_Search.py
import re
# 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
match = re.search(r'[1-9]\d{5}', 'BIT 100051')
# 如果match为空，则判断为False
if match:
    # print('In match')
    print(match.group(0))