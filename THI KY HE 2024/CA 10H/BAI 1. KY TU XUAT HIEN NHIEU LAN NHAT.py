for _ in range(int(input())):
    s = input()
    d = dict()
    for x in s:
        if x in d: d[x]+=1
        else: d[x] = 1 
    res = list(d.items())
    y = -1
    for x in res: y = max(y, x[1])
    for x in res:
        if x[1]==y:
            print(x[0])
            break 
