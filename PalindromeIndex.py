def isPalindrome(s):
    r = s[::-1]
    if s == r:
        return True
    return False

s = input()
# if isPalindrome(s):
#     return -1
# else:
#     for i in range(0, len(s)):
#         t = s[0:i] + s[i+1:]
#         if isPalindrome(t):
#             return i
#     return -1