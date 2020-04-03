class DemoClass:
    count = 0
    def __init__(self, name, age):
         self.name = name
         self.age = age
         DemoClass.count += 1
     # 自由方法
    def foo():
        DemoClass.count *= 100
        return DemoClass.count
    # 实例方法lucky()，由实例对象独享
    def lucky(self):
        s = 0
        for c in self.name:
            s += ord(c) % 100
        return s
    # 类方法getChrCount()
    @classmethod
    def getChrCount(cls):
        s = '零一二三四五六七八九'
        return s[(DemoClass.count) % 10]
class DemoClass2:
    count = 0
    def __init__(self, name):
        self.name = name
        DemoClass2.count += 1
    # 保留方法
    def __len__(self):
        return len(self.name)
    # 自自由方法
    def foo():
        DemoClass2.count *= 10
        return DemoClass2.count
    # 静态方法
    @staticmethod
    def fooSt():
        DemoClass2.count /= 10
        return DemoClass2.count

dc1 = DemoClass('老A', 45)
dc2 = DemoClass('老B', 66)
print('count=', DemoClass.count)
print(dc1.name, dc2.name)
print(dc1.count, dc2.count)
# 实例方法
print('{}的幸运数字为：{}'.format(dc1.name, dc1.lucky()))
print('{}的幸运数字为：{}'.format(dc2.name, dc2.lucky()))
print(type(dc1.count))
# 类方法
print(dc1.getChrCount())
dc3 = DemoClass('老C', 18)
print(DemoClass.getChrCount())
# 自由方法
x = DemoClass.foo()
print(x)
dc2_1 = DemoClass2('小花a')
print(DemoClass2.foo())
# print(dc2_1.foo())    # 不可使用对象名调用自由方法
# 调用静态方法
print(DemoClass2.fooSt())   #通过类名调用
print(dc2_1.fooSt())        #通过实例名调用
# 调用保留方法
print(dc2_1.__len__())
print(len(dc2_1))  #Pyhton解释器保留方法，已对应，只需编写代码即可