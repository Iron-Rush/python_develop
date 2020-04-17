# OverloadDemo_Count.py
# 继承list类型的新类型
# 重载其中的加法运算
class NewList(list):
    "二元算术运算符的重载"
    def __add__(self, other):
        result = []
        for i in range(len(self)):
            # 若other比self短，则在rusult后直接追加self[i]
            try:
                result.append(self[i] + other[i])
            except:
                result.append(self[i])
        return result

    # 比较运算的重载
    def __lt__(self, other):
        "以个元素之和为比较依据"
        s, t = 0, 0
        for c in self:
            s += c
        for c in other:
            t += c
        return True if s < t else False

    # 成员判断的重载
    def __contains__(self, item):
        s = 0
        for c in self:
            s += c
        if super().__contains__(item) or item == s:
            return True
        else:
            return False
    # 格式化输出重载
    def __format__(self, format_spec):
        "格式化输出，以逗号分隔"
        t = []
        for c in self:
            if type(c) == type("字符串"):
                t.append(c)
            else:
                t.append(str(c))
        return ", ".join(t)

ls = NewList([1,2,3,4,5,6])
lt = NewList([1,2,3,4])
print(ls + lt)  # [2, 4, 6, 8, 5, 6]
print(ls < lt)
print(4 in lt, 10 in lt)    # True True
print(format(lt))   # 1，2，3，4
print([1,2,3,4])    # [1, 2, 3, 4]