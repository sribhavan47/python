def asec(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            return False
    return True
a=[1,3,2,5,7,9]
print(asec(a))