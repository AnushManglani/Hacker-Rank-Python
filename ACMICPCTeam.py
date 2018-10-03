d = ['10101', '11100', '11010', '00101']
e = []
for i in range(0, len(d)):
    for j in range(i + 1, len(d)):
        e.append(int(d[i], 2) | int(d[j], 2))
print(bin(max(e))[2:].count('1'))
print(e.count(max(e)))