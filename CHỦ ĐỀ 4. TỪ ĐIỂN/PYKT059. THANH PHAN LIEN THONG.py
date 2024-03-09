def DFS(x, visited, ke):
    visited[x] = 1 
    for i in ke[x]:
        if visited[i] ==0: DFS(i, visited, ke)
visited = [0] * 1005
ke = [[] for _ in range (1005)]
dinh, canh, x = map(int, input().split())
for i in range (canh):
    dau, cuoi = map(int, input().split())
    ke[dau].append(cuoi)
    ke[cuoi].append(dau)
DFS(x, visited, ke)
for i in range (1, dinh + 1):
    if visited[i] ==0: print(i)