for _ in range(int(input())):
    hang, cot = map(int, input().split())
    a = []
    for _ in range(hang):
        b = list(map(int, input().split()))
        a.append(b)
    b = [[0] * hang for _ in range(cot)]  
    for i in range(cot):
        for j in range(hang): b[i][j] = a[j][i]
    res = [[0] * hang for _ in range(hang)]
    for i in range(hang):
        for j in range(hang):
            for k in range(cot): res[i][j] += a[i][k] * b[k][j]
    for i in range(hang):
        for j in range(hang): print(res[i][j], end=" ")
        print()