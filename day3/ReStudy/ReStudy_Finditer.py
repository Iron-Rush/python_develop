# ReStudy_Finditer.py
import re
# 搜索字符串，返回一个匹配结果的迭代类型，迭代元素为match对象
for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
    if m:
        print(m.group(0))