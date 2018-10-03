s = "c"
d = list(s)
pivot = -1
for i in range(len(d)-1, 0, -1):
    if ord(d[i]) > ord(d[i-1]):
        pivot = i - 1
        break
# print(pivot)
if len(s) == 1:
    print("no answer")
elif pivot == -1:
    print("no answer")
else:
    for i in range(len(d)-1, pivot, -1):
        if ord(d[i]) > ord(d[pivot]):
            d[d.index(d[i])], d[d.index(d[pivot])] = d[d.index(d[pivot])], d[d.index(d[i])]
            break
    for j in range(pivot+1, int((len(d)+pivot+1)/2)):
        d[j], d[len(d)+pivot-j] = d[len(d)+pivot-j], d[j]
print(''.join(d))