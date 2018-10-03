numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
st = input("String: ")

d = [0, 0, 0, 0]
for i in st:
    if i in numbers:
        d[0] = d[0] + 1
    elif i in lower_case:
        d[1] = d[1] + 1
    elif i in upper_case:
        d[2] = d[2] + 1
    else:
        d[3] = d[3] + 1
if len(st) >= 6:
    print(d.count(0))
elif len(st) < 6:
    print(max(d.count(0), 6-len(st)))