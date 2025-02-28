from re import match
def temperatureConvertor(a,type):
    match type:
        case 0:
            return (a*9/5)+32
        case 1:
            return a+273
        case 2:
            return (a-32)*5/9
        case 3:
            return ((a-32)*5/9)+273
        case 4:
            return a-273
        case 5:
            return ((a-273)*9/5)+32
a=int(input("value: "))
b=int(input("type: "))
print(temperatureConvertor(a,b))