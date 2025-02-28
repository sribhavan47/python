def palindrome(s):
    a=""
    for i in range(len(s)-1,-1,-1):
        a+=s[i]
    return a==s
s=input()
print(palindrome(s))