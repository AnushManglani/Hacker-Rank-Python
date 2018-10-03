s = "saveChangesInTheEditor"
k = 1
for i in range(0, len(s)):
    if ord(s[i]) in range(65, 91):
        k = k + 1
print(k)