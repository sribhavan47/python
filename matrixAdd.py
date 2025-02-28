def add(x,y):
    result=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(x)):
        for j in range(len(x)):
            result[i][j]=x[i][j]+y[i][j]
    return result

def transpose(x):
    result=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(x)):
        for j in range(len(x)):
            result[i][j]=x[j][i]
    return result

x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,3],[4,5,6],[7,8,9]]
print(add(x,y))
print(transpose(x))
