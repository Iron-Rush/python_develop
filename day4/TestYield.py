# TestYield.py
# 生成器写法(每次返回一个值)
def gen(n):
    for i in range(n):
        yield i**2
# 普通写法(放到列表中一起返回)
def square(n):
    ls = [i**2 for i in range(n)]
    return ls
for i in gen(5):
    print(i, " ", end='')


print()
for i in square(5):
    print(i, " ", end='')