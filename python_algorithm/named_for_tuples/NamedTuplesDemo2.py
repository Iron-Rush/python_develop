# NamedTuplesDemo2.py
from collections import namedtuple
# 命名工厂
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s1 = Student('Tom', 16, 'male', 'Tom16@gmail.com')
print(s1)