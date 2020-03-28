# ReStudy_Sub.py
import re
# 在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
# count为匹配的最大替换次数
subStr = re.sub(r'[1-9]\d{5}', 'zipcode', 'BIT100081 TSU100084', count=1)
print(subStr)