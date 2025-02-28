def permute(s, s2,a):
    if ((s2) not in a):
        a.append(s2)
        print(s2)
    
    for i in range(len(s)):
        char = s[i]
        left_s = s[0:i]
        right_s = s[i+1:]
        rest = left_s + right_s
        permute(rest, s2 + char,a)

s1 = "zsf"
s2 = ""
a=[]
permute(s1, s2,a)