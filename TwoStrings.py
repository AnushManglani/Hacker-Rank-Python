s = "Hello"
t = "World"
a = set(list(s))
b = set(list(t))
c = a.intersection(b)
if len(c) > 0:
    print("YES")
else:
    print("NO")
