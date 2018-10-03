s = input().strip()
s = s.replace(" ", "")
s = s.lower()
if len(set(s)) == 26:
    print("pangram")
else:
    print("not pangram")