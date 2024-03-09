for _ in range(int(input())):
    n = int(input())
    d = dict()
    a = list(map(int, input().split()))
    for x in a:
        if x in d: d[x]+=1 
        else: d[x] = 1 
    b = list(d.items())
    b.sort(key = lambda x: (-x[1], x[0]))
    if b[0][1] <= n/2: print("NO")
    else: print(b[0][0])

