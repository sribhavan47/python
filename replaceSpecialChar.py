def replace(s):
    b=''
    for i in s:
        if i.isalnum():
            b+=i
        else:
            b+=''
    return b
a=input()
print(replace(a))