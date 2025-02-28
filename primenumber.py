def primenumber(a):
    for i in range(2,a//2):
        if a%i==0:
            return False
        break
    return True
a=int(input())
print(primenumber(a))