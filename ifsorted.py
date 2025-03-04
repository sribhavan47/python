def ifsort(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            return False
    return True
a=[1,2,3,5,4,4,5]
print(ifsort(a))