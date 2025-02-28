def mergesort(a):
    if len(a)>1:
        mid=len(a)//2
        left=a[:mid]
        right=a[mid:]
        mergesort(left)
        mergesort(right)
        merge(a,left,right)
    return a

def merge(a,left,right):
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            a[k]=left[i]
            i+=1
        else:
            a[k]=right[j]
            j+=1
        k+=1
    
    while i<len(left):
        a[k]=left[i]
        i+=1
        k+=1

    while j<len(right):
        a[k]=right[j]
        j+=1
        k+=1

a=[1,3,4,2,5,6]
print(mergesort(a))