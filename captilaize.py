def captilaize(s):
    return s[0].upper()+s[1:-1]+s[-1].upper()
a=input()
print(captilaize(a))