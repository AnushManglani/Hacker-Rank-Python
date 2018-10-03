import collections
s = "cdefghmnopqrstuvw"
a = list(s)
count = collections.Counter(a)
d = list(count.values())
flag = 0
stat = 1
for i in d:
    if i % 2 == 1 and flag == 0:
        flag = 1
    elif i%2 == 1 and flag == 1:
        stat = 0
        break
if stat == 1:
    print("YES")
else:
    print("NO")