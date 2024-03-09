from sys import stdin
a = []
for line in stdin:
    b = list(map(int, line.strip().split()))
    for x in b: a.append(x)
t = a[0]
a.pop(0)
for _ in range(t):
    hang = a[0]; a.pop(0)
    cot = a[0]; a.pop(0)
    x = [[0] * cot for _ in range (hang)]
    y = [[0] * hang for _ in range (cot)]
    for i in range(hang):
        for j in range(cot):
            x[i][j] = a[0]
            a.pop(0)
    z = [[0] * hang for _ in range (hang)]
    for i in range(cot):
        for j in range(hang): y[i][j] = x[j][i]
    for i in range(hang):
        for j in range(hang):
            for k in range(cot): z[i][j]+=x[i][k] * y[k][j]
    for i in range(hang):
        for j in range(hang): print(z[i][j], end = " ")
        print()