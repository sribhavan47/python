def binary(a,tar):
    middle=a[len(a)//2]
    left=[]
    right=[]
    if middle==tar:
        return middle
    else:
        left=a[:middle]
        right=a[middle+1:]
    return binary(left,tar),binary(right,tar)
a=[1,3,5,8,3,9,0]
tar=0
print(binary(a,tar))