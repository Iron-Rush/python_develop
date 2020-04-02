# DictFilter.py
# 在字典中根据条件筛选数据
# 生成随机字典
from random import randint
d = {x: randint(60, 100) for x in range(1, 21)}
print(d)
# 字典解析
d1 = {k: v for k, v in d.items() if v > 90}
print(d1)