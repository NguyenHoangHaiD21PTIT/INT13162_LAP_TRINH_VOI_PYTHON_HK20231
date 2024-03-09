hang, cot = map(int, input().split())
a = []
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range (hang):
    b = list(map(int, input().split()))
    a.append(b)
tong = 0
q = []
for i in range (hang):
    for j in range (cot):
        if(a[i][j]==-1): q.append([i, j])
while q:
    u = q[0]
    q.pop(0)
    for k in range (0, 8):
        i1 = u[0] + dx[k]
        j1 = u[1] + dy[k]
        if 0<= i1 < hang and 0 <= j1 < cot and a[i1][j1] != 0: 
            tong+=a[i1][j1]
            a[i1][j1] = 0
    
print(tong)