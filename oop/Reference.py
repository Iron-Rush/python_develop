# Reference.py
# 可变对象的引用：列表
ls = [1, 2, 3, 4]
lt = ls
print(id(ls), id(lt))

# 不可变对象的引用：字符串
a1 = "Python计算生态"
a2 = a1
a3 = "Python计算生态"
b1 = "Python"
b2 = "计算生态"
b3 = b1 + b2
print(id(a1), id(a2), id(a3))
print(id(b1), id(b2), id(b3))
la = [1, 2]
lb = la
la.append(3)
print(la, lb, id(la), id(lb))   #la == lb