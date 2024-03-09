for i in range(int(input())) :
    ok = 1
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(n) :
        if a[i] > b[i] :
            ok = 0
            break
    if ok == 1 : print("YES")
    else : print("NO")