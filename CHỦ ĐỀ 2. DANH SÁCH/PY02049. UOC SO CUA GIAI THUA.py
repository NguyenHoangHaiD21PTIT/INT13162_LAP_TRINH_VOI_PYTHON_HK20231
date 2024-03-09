for _ in range(int(input())):
    n, p = map(int, input().split())
    cnt = 0
    for i in range(1, n + 1):
        tmp = i
        while tmp%p==0:
            tmp//=p 
            cnt+=1 
    print(cnt)