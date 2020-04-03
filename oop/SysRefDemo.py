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
# 获取当前对象引用次数(获取时会导致访问量+1)
print(sys.getrefcount(dc1))     # 三个引用分别为dc1、dc2、refcount
del dc1     #关闭dc1的引用
print(sys.getrefcount(dc2))