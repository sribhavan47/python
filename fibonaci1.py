def fibonaci(a):
    s=[0]*a
    s[0]=0
    s[1]=1
    for i in range(2,a):
        s[i]=s[i-1]+s[i-2]
    return s[-1]
a=int(input())
print(fibonaci(a))