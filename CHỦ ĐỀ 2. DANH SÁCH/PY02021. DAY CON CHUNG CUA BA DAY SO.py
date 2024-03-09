for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a, b, c = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))
    p1, p2, p3, ok = 0, 0, 0, 0
    while p1 < n and p2 < m and p3 < k:
        if a[p1] == b[p2] and b[p2] == c[p3]:
            ok = 1 
            print(a[p1], end = ' ')
            p1, p2, p3  = p1 + 1, p2 + 1, p3 + 1 
        elif a[p1] <= b[p2] and a[p1] <= c[p3]: p1+=1 
        elif b[p2] <= a[p1] and b[p2] <= c[p3]: p2+=1 
        else: p3+=1 
    if ok == 0: print("NO", end = '')
    print()