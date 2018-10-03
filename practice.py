from Crypto.Cipher import DES

s = b'caaabfgh'
key = b'asdfghjk'
des = DES.new(key, DES.MODE_ECB)
s = des.encrypt(s)
print(s)
a = list(s)
print(list(set(a)))

# print(s[0:4])
# a = "ffbbxx"
# b = "xaxbeejsbdjhcsbdhb"
# d = list(b)
# d.sort()
# print(d)
# e= 5
# f =6
# e, f = f, e
# print(e, f)
# print(b[0:len(b)-3], b[-3:])
# al = list(a)
# bl = list(b)
# print(al)
# print(bl)
# for i in al:
#     if i in bl:
#         bl.remove(i)
#         print(bl)
# print(al.intersection(bl))
# print(set().intersection(al, bl))
# print(s.find("aa", s.find("aa")+1))
# st = set(s)
# print(len(st))
