import math
s = "iffactsdontfittotheorychangethefacts"
r = int(math.sqrt(len(s)))
if r*r == len(s):
    c = r
elif r*r < len(s):
    c = r+1
    while r * c < len(s):
        if r < c:
            r = r + 1
        else:
            c = c + 1

print(r, c, r*c, len(s))
st = ""
k = 0
for i in range(0, c):
    for j in range(0, r):
        if (c*j + i) < len(s):
            st = st + s[c*j + i]
    st = st + " "
print(st)