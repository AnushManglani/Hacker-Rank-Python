s = "bcdybc"
g = ["a", "b", "c", "aa", "d", "b"]
h = [1, 2, 3, 4, 5, 6]
f = 2
l = 4
su = 0
for i in range(f, l + 1):
    k = 0
    while s.find(g[i], k) > -1:
        k = s.find(g[i], k) + 1
        su = su + h[i]

print(su)