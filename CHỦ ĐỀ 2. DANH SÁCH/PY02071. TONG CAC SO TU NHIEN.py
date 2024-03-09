def kt():
    global cnt
    cnt = 1
    a[1] = n

def sinh():
    global cnt, ok
    i = cnt
    while i >= 1 and a[i] == 1:
        i -= 1
    if i == 0:
        ok = 0
    else:
        a[i] -= 1
        bu = (cnt - (i + 1) + 1) + 1
        cnt = i
        q = bu // a[i]
        r = bu % a[i]
        if q != 0:
            for _ in range(q):
                cnt += 1
                a[cnt] = a[i]
        if r != 0:
            cnt += 1
            a[cnt] = r

t = int(input())
for _ in range(t):
    n = int(input())
    ok = 1
    a = [0] * 100
    kt()
    res = []
    while ok == 1:
        s = "("
        for i in range(1, cnt):
            s += str(a[i]) + " "
        s += str(a[cnt]) + ")"
        res.append(s)
        sinh()
    print(len(res))
    for x in res:
        print(x, end=" ")
    print()