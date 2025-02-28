def harmonic(a):
    har_n=len(a)
    har_de=0
    for i in a:
        har_de+=1/i
    return har_n/har_de

def geometric(a):
    prod=1
    for i in a:
        prod*=i
    return prod**(1/len(a))

a=[6,7,3,9,10,15]
print(harmonic(a))
print(geometric(a))