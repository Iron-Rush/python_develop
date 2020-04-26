# Copy.py
ls = ["Python", [1, 2, 3]]
la = ls.copy()
lb = ls[:]
lc = list(ls)

print("ls", id(ls))
print("la", id(la))
print("lb", id(lb))
print("lc", id(lc))