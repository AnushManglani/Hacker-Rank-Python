import collections
s = "aaaabbcc"
t = list(s)
count = collections.Counter(t)
# print(count)
d = list(count.values())
e = collections.Counter(d)
f = list(e.values())
g = list(e.keys())
if len(f) > 2:
    print("NO")
elif len(f) == 1:
    print("YES")
elif 1 not in f:
    print("NO")
elif g[f.index(1)] == 1 or g[f.index(1)] - g[(f.index(1)+1) % 2] == 1:
    print("YES")
else:
    print("NO")

