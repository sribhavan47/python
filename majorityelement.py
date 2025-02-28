from collections import defaultdict
def majority(a):
    candidtae=-1
    votes=0
    for i in a:
        if votes==0:
            candidtae=i
        if i==candidtae:
            votes+=1
        else:
            votes-=1
    return candidtae
a=[1,2,3,3,4,4,4,4,4,4,4,3,3]
print(majority(a))
