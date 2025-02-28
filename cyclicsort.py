def cyclicsort(a):
    mini=min(a)
    for i in range(len(a)):
        while a[i]!=i+mini:
            crct_index=a[i]-mini
            a[i],a[crct_index]=a[crct_index],a[i]
    return a
a=[4,3,5,8,7,6]
print(cyclicsort(a))