# TestEmptyClass.py
class EmptyClass:
    pass
a = EmptyClass()
a.name = "老王"
a.age = 50
a.family = {"儿子": "小王", "女儿": "二王"}
a.ls = [10,15,20]
print(a.family)
print(a.__dict__)