def hackerrankInString(s):
    c = 0
    j = 0
    test = "hackerrank"
    for i in s:
        print(i)
        if c == 10:
            break
        try:
            if test[j] == i:
                c = c + 1
                # print(test[j], c)
                j = j + 1
        except:
            # print(j)
            pass
    if c == 10:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        hackerrankInString(s)
