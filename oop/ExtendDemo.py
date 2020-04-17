# ExtendDemo
# 基类派生类demo

# 基类
class DemoClass:
    count = 0
    def __init__(self, name):
        self.name = name
        DemoClass.count += 1

    def getName(self):
        return self.name
# 派生类
class HumanNameClass(DemoClass):
    def printName(self):
        return str(DemoClass.count) + self.name + '同志'

dc1 = HumanNameClass('老王A')
dc2 = HumanNameClass('老张B')
print('getName：', dc1.getName(), '\tprintName：', dc1.printName())
print('getName：', dc2.getName(), '\tprintName：', dc2.printName())
print(dc1 is dc2)
dc3 = dc1
print(dc3 is dc1)
print("dc1 ID:{},dc2 ID:{},dc3 ID:{}".format(id(dc1), id(dc2), id(dc3)))