a = [1, 2, 4, 5, 7, 8, 10]
d = 3
flag = 0
count = 0
for i in range(0, len(a)):
    flag = 0
    for j in range(i+1, len(a)):
        if a[i]+d == a[j] and flag == 0:
            flag = 1
        if flag == 1 and a[i]+2*d == a[j]:
            flag = 2
        if flag == 2:
            count = count + 1
            break
print(count)