s = input()
c = 0
for i in range(0, int(len(s)/2)):
    c = c + (abs(ord(s[i]) - ord(s[len(s)-1-i])))
print(c)