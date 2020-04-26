# NameMangling.py
# 类中名称的变换约定
class DemoClass:
    def __init__(self, name):
        self.name = name
        self._nick = name + "同志"
        self.__nick1__ = name + "A"
        self.__nick = name + "老铁"
        self.class_ = name = "班"

    def getNick(self):
        return self._nick
    def __nick__(self):
        return self.__nick1__

dc1 = DemoClass("老李")
print(dc1.getNick())    # 老李同志
print(dc1._nick)        # 老李同志
print(dc1._DemoClass__nick) # 老李老铁
# print(dc1.__nick)       # AttributeError: 'DemoClass' object has no attribute '__nick'
print(dc1.__nick__())   # 老李A