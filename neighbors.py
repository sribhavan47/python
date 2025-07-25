from collections import defaultdict
def find_neighbors(x,y):
    a=defaultdict(list)
    for i,j in x:
        a[i].append(j)
        a[j].append(i)
    res=[]
    for i in y:
        res.append(a[i])
    return res

x=[(1, 2), (2, 3), (3, 4), (4, 5)]
y=[1, 2, 3, 5]
print(find_neighbors(x,y))