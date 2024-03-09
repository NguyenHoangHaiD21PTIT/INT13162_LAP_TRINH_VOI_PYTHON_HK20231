n = int(input())
for _ in range (n):
    tmp = "x^+"
    s = input()
    for x in tmp: s = s.replace(x, " ")
    a = list(map(int, s.split()))
    d = dict()
    for i in range (0, len(a), 2): 
        if a[i + 1] in d: d[a[i + 1]]+=a[i]
        else: d[a[i + 1]] = a[i]
    res = list(d.items())
    res.sort(key = lambda x: x[0])
    ans = ""
    for x in res: 
        tmp = str(x[1]) + "x^" + str(x[0])
        ans += tmp + " + "
    print(ans[:-2:])