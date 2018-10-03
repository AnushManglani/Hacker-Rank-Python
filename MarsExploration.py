s = input("String: ")
d = ['S', 'O', 'S']
c = 0
for i in range(0, len(s)):
    if s[i] != d[i % 3]:
        c = c + 1

print(c)
