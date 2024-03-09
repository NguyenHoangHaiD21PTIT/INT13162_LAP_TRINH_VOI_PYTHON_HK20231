for _ in range(int(input())):
    s = input()
    tong = 0
    res = []
    for x in s:
        if x.isalpha(): res.append(x)
        else: tong+=int(x)
    res.sort()
    for x in res: print(x, end = "")
    print(tong)