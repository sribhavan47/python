def fibonaci(a):
    if a==0:
        return 0
    if a==1:
        return 1
    else:
        return fibonaci(a-1)+fibonaci(a-2)
a=int(input())
print(fibonaci(a))