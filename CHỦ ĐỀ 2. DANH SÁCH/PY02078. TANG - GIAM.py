for _ in range(int(input())):
    n = int(input())
    a = []
    b = []
    f = [1] * n
    
    for i in range(n):
        ai, bi = map(float, input().split())
        a.append(ai)
        b.append(bi)
        
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and b[j] > b[i]:
                f[i] = max(f[i], f[j] + 1)
                
    print(max(f))