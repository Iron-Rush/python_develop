# NamedTuplesDemo1.py
# NAME = 0
# AGE = 1
# SEX = 2
# EMAIL = 3
NAME, AGE, SEX, EMAIL = range(4)

student = ('Tom', 16, 'male', 'Tom16@gmail.com')
# name
print(student[0])
print(student[NAME])

# AGE
print(student[1])
print(student[AGE])

# SEX
print(student[2])
print(student[SEX])

# EMAIL
print(student[3])
print(student[EMAIL])