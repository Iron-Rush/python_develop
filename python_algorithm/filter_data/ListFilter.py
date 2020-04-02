# ListFilter.py
# 在列表中根据条件筛选数据
# import timeit
# 生成随机列表
from random import randint
data = [randint(-10, 10) for _ in range(10)]
print(data)
# 通用
res = []
for x in data:
    if x >= 0:
        res.append(x)
print(res)
# 1.filter
# 1、循环帮你调用函数
# 2、帮你过滤你传入的参数，函数的结果返回的是true那就保存
# 返回false就不要，且返回的也是迭代器
ls1 = list(filter(lambda x: x>= 0, data))
print(ls1)
# 2.列表解析(速度最快)
ls2 = [x for x in data if x >= 0]
print(ls2)
# print(timeit.timeit(filter(lambda x: x>= 0, data)))
# t2 = timeit.timeit([x for x in data if x >= 0])
'''
    列表解析更为迅速，为filter的一半时间
'''