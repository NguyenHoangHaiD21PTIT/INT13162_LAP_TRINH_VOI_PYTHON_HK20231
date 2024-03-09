n = int(input())
a = []
for _ in range (n):
    b = list(map(int, input().split()))
    a.append(b)
f = [0] * 1000
for j in range(n): f[a[0][j]] = 1
for i in range (1, n):
    for j in range (n):
        if f[a[i][j]] == i: f[a[i][j]] = i + 1         
res = []
for j in range (0, n):
    if f[a[n - 1][j]] == n and a[n - 1][j] not in res: res.append(a[n - 1][j])
res.sort()
if len(res) == 0: print("NOT FOUND")
for x in res: print(x, end  =" ")