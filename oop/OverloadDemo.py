# OverloadDemo.py
# 类的属性重载

class DemoClass:
    count = 0
    def __init__(self, name):
        self.name = name
        DemoClass.count += 1

class HumanNameClass(DemoClass):
    count = 99
    def __init__(self, name):
        self.name = name
        HumanNameClass.count -= 1
    def printCount(self):
        return str(HumanNameClass.count) + self.name

dc1 = HumanNameClass("老王")
print(dc1.printCount()) # 98老王