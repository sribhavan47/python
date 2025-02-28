def revrese(s):
    s=list(s)
    index=len(s)-1
    i=0
    while index>i:
        s[i],s[index]=s[index],s[i]
        index-=1
        i+=1
    s="".join(s)
    return s
s="abcd"
print(revrese(s))