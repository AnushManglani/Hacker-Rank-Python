test = int(input())
for _ in range(0, test):
    l = int(input())
    d = input().split()
    i = 0
    j = l-1
    m = 0
    s =0
    p=0
    while True:
        if j - i == 1:
            m = m + 1
            p = p +1
            break
        else:
            value = 2 * int(d[j])
            p = p + 1
            j = j - 1
            while True:
                s = s + int(d[i])
                i = i + 1
                m = m + 1
                if s > value:
                    s = s - value
                    if s == 0:
                        i = i-1