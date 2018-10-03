d = ["abcdde", "baccd", "eeabg"]
s = set(d[0])

for i in range(1, len(d)):
    s = s.intersection(set(d[i]))

print(len(s))