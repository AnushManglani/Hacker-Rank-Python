d = [7, 1, 3, 4, 1, 7]
minn = 10000000
for i in range(0, len(d)):
    for j in range(i+1, len(d)):
        if d[j] == d[i]:
            if j-i < minn:
                minn = j-i
print(minn)