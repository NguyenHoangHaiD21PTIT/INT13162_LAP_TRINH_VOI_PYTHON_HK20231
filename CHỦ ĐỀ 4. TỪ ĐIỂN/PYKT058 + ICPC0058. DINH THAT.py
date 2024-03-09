def DFS(x, visited, ke):
    visited[x] = 1 
    for i in ke[x]:
        if visited[i]==0: DFS(i, visited, ke)

for _ in range (int(input())):
    dinh, canh, u, v = map(int, input().split())
    visited = [0] * 1005
    ke = [[] for _ in range (1005)]
    for _ in range(canh):
        dau, cuoi = map(int, input().split())
        ke[dau].append(cuoi)
    #Xét từng đỉnh, ta chặn đỉnh ấy lại, DFS(u) xem v đến được hay không
    res = 0
    for i in range (1, dinh + 1):
        visited = [0] * 1005 #Mỗi lần xong phải reset lại mảng 
        visited[i] = 1 
        DFS(u, visited, ke)
        if visited[v] ==0: res+=1 
    print(res)