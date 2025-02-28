def bubblesort(a):
    n=len(a)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swapped=True
        if not swapped:
            break
    return a
a=[1,4,6,2,5,7,9]
print(bubblesort(a))