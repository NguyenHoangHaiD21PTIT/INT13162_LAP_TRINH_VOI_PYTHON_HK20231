while True :
    a = list(map(int, input().split()))
    if a == [0, 0, 0, 0]: break
    cnt = 0
    while True:
        if a[0] == a[1] and a[1] == a[2] and a[2] == a[3] :
            print(cnt)
            break
        p = a[0]
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = abs(a[3] - p)
        cnt+=1
