for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l = [-1] * n
    st1 = []  
    for i in range(n):
        while st1 and a[i] >= a[st1[-1]]: st1.pop()
        if not st1: l[i] = -1
        else: l[i] = st1[-1]
        st1.append(i)
    r = [-1] * n
    st2 = []
    for i in range(n - 1, -1, -1):
        while st2 and a[i] < a[st2[-1]]: st2.pop()
        if not st2: r[i] = -1
        else: r[i] = st2[-1]
        st2.append(i) 
    res = 0
    for i in range(n):
        if l[i] == -1 and r[i] == -1: res += 1
    print(res)