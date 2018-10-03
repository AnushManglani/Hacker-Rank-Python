a = [5, 2, 1, 3, 4]
b = []
k = 0
for i in range(1, len(a) + 1):
    k = 0
    while True:
        if i != a[k]:
            k = k + 1
        else:
            b.append(a.index(k + 1)+1)
            break
print(b)
