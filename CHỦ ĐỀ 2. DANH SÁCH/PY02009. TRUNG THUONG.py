for _ in range(int(input())):
    n = int(input())
    a = []
    d = dict()
    for i in range(n):
        x = int(input())
        if x in d: d[x] += 1 
        else: d[x] = 1 
    res = list(d.items())
    res.sort(key = lambda x: (-x[1], x[0]))
    print(res[0][0])

