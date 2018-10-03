s = "fcrxzwscanmligyxyvym"
t = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
a = list(s)
b = list(t)
print(a, b)
i=0
while i < len(a):
    if a[i] in b:
        print(a[i])
        try:
            a.remove(a[i])
            b.remove(a[i])
        except:
            print(i, a[i])
        i = i-1
    i = i+1
print(a, b)
# fcrxzwscanmligyxyvym
# jxwtrhvujlmrpdoqbisbwhmgpmeoke