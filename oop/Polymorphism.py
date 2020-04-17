# Polymorphism.py
# 参数类型的多态
# 一个方法能够处理多个类型的能力
# 一个方法能够接受多个参数的能力
class DemoClass:
    def __init__(self, name):
        self.name = name
    def __id__(self):
        return len(self.name)

    def lucky(self, salt, more = 9):
        # print("more=", more)
        s = 0
        for c in self.name:
            s += (ord(c) + id(salt) + more) % 100
        return s

dc = DemoClass("老王")
print(dc.lucky(10))
print(dc.lucky("10"))
print(dc.lucky(dc))
print(dc.lucky(10, 100))