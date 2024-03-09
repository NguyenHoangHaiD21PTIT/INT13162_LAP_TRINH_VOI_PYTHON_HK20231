t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = []
    h = [[0] * 3 for _ in range(3)]
    y = [[0] * (m - 2) for _ in range(n - 2)]
    res = 0

    for i in range(n):
        x.append(list(map(int, input().split())))

    for i in range(3):
        h[i] = list(map(int, input().split()))

    for i in range(n - 2):
        for j in range(m - 2):
            y[i][j] = sum(h[k][l] * x[k + i][l + j] for k in range(3) for l in range(3))

    res = sum(sum(row) for row in y)

    print(res)