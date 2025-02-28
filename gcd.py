def gcd(a,b):
    c=max(a,b)
    d=min(a,b)
    while d>0:
        e=d
        d=c%d
        c=e
    return c
a=int(input())
b=int(input())
print(gcd(a,b)) 