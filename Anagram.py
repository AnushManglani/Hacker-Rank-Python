s = input()
if len(s) % 2 == 1:
    print(-1)
else:
    a = list(s[0:int(len(s)/2)])
    b = list(s[int(len(s)/2):])
    for i in a:
        if i in b:
            b.remove(i)
    print(len(b))