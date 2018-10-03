import math
s = "bcxy"
flag = 0
d = []
st = s[::-1]
for i in range(1, len(s)):
    d.append(abs(ord(s[i-1]) - ord(s[i])))

for i in range(1, len(st)):
    if d[i-1] != abs(ord(st[i-1])-ord(st[i])):
        flag = 1
        break

if flag == 1:
    print("not funny")
else:
    print("funny")