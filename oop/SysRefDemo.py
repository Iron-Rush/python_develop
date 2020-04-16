# SysRefDemo.py
# Python引用和垃圾回收机制
import sys
class DemoClass:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print("再见" + self.name)
        # return "再见" + self.name
dc1 = DemoClass('老王')
dc2 = dc1
dc2.name = '老八' 
print(dc2.name, sys.getrefcount(dc2))
print(dc1.name, sys.getrefcount(dc1))
# 获取当前对象引用次数(获取时会导致访问量+1)
print(sys.getrefcount(dc1))     # 三个引用分别为dc1、dc2、refcount
del dc1     #关闭dc1的引用
print(sys.getrefcount(dc2))
x = 50
print('x=', x, 'x的引用次数:', sys.getrefcount(x))
y = x
print('x=', x, 'x的引用次数1:', sys.getrefcount(x))
x += 1
print('x=', x, 'x的引用次数2:', sys.getrefcount(x))
print('y=', y, 'y的引用次数1:', sys.getrefcount(y))