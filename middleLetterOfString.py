def middle(s):
    if len(s)%2==0:
        return s[len(s)//2-1],s[len(s)//2]
    return s[len(s)//2]
s=input()
print(middle(s))