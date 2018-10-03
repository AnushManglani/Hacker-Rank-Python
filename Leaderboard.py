a = [2, 1]
b = [1, 1]
c = []
k = 1


for y in range(0, len(b)):
    k = 1
    for x in range(1, len(a)):
        if b[y] >= a[0]:
            k = 0
            print("k is " + str(k))
            break
        if a[x] != a[x-1] and a[x] > b[y]:

            k = k+1
        if a[x] < b[y]:
            break
    c.append(k+1)
print(c)

