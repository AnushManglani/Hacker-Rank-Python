def validate(seq):
    for i in range(0, len(seq) - 1):
        if seq[i] == seq[i + 1]:
            return False
    return True


s = input().strip()
st = list(set(s))
l = 0
for x in range(len(st)):
    for y in range(x + 1, len(st)):
        seq = [c for c in s if c == st[x] or c == st[y]]
        if validate(seq):
            l = max(l, len(seq))
print(l)
