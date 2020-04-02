# SetFilter.py
# 在集合中根据条件筛选数据
# 生成随机列表
from random import randint
data = [randint(-10, 10) for x in range(10)]
s = set(data)
print(s)
# 集合解析
# 返回能被3整除的数
s1 = {x for x in s if x % 3 == 0}
print(s1)