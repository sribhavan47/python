from collections import defaultdict
def concate(d1,d2):
    d3=defaultdict(int)
    for i,j in d1.items():
        d3[i]+=j
    for i,j in d2.items():
        d1[i]+=j
    return d1
d1=defaultdict(int)
d1['a']=3
d1['b']=2
d1['c']=1
d2={'a':1,'b':3,'d':1}
print(concate(d1,d2))
