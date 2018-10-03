st = input("String: ")
k = int(input("k :"))
s = ""
for i in st:
    ch = ord(i)
    if ch in range(65, 91):
        ch = 65 + (ch - 65 + k) % 26
    if ch in range(97, 123):
        ch = 97 + (ch - 97 + k) % 26
    s = s + chr(ch)
print(s)
