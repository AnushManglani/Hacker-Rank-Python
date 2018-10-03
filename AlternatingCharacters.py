s = "AAABBB"
c = 0
for i in range(0, len(s)-1):
    if s[i] == s[i+1]:
        c = c + 1
print(c)