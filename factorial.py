def factorial(a):
    s=[0]*(a+1)
    s[0]=1
    for i in range(1,a+1):
        s[i]=i*s[i-1]
    return s[-1]
a=int(input())
print(factorial(a))