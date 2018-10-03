def kaprekarNumbers(p, q):
    flag = 0
    for i in range(p, q + 1):
        s = str(i * i)
        if len(str(i)) == 1 and len(s) == 1:
            if str(i) == s:
                print(i, end=' ')
                flag = 1
        elif len(s) >= 2 * len(str(i)) - 1:
            d = int(s[0:len(s)-len(str(i))]) + int(s[-len(str(i)):])
            if d == i:
                print(i, end=' ')
                flag = 1
    if flag == 0:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)