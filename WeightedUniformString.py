def weightedUniformStrings(s, queries):
    d = [0] * 10000000
    mul = 1
    prev = ""
    for i in range(0, len(s)):
        ch = ord(s[i]) - 96
        if s[i] == prev:
            mul = mul + 1
            ch = ch * mul
        else:
            mul = 1
        prev = s[i]
        d[ch] = 1

    for i in queries:
        if d[i] == 1:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    s = input()
    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    weightedUniformStrings(s, queries)
