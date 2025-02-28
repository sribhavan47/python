#4.	program to test a number is a prime number
def amstrongnumber(a):
    c=a
    i=0
    b=0
    while a>0:
        b+=(a%(10))**3
        a=a//10
        i+=1
    return b==c
a=int(input())
print(amstrongnumber(a))
