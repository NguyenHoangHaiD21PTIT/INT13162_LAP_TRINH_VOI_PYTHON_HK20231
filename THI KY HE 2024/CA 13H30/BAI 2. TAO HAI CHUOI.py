for _ in range(int(input())):
    s = input()
    d = dict()
    for x in s:
        if x in d: d[x]+=1
        else: d[x] = 1 
    s1, s2 = [], []
    res = list(d.items())
    for x in res:
        if x[1]>=2: s2.append(x[0])
        else: s1.append(x[0])
    s1.sort()
    s2.sort()
    if len(s1)==0: print("NONE")
    else: 
        for x in s1: print(x, end="")
        print()
    if len(s2)==0: print("NONE")
    else: 
        for x in s2: print(x, end="")
        print()
'''
2
aabbcceffgh
abcabc
'''