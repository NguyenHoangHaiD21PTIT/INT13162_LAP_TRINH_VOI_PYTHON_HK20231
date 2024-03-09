def DFS(x, visited, ke):
    visited[x] = 1 
    for i in ke[x]:
        if visited[i] == 0: DFS(i, visited, ke)
        
for _ in range(int(input())):
    dinh, canh = map(int, input().split())
    visited = [0] * 1005
    ke = [[] for _ in range (1005)]
    for i in range (canh):
        dau, cuoi = map(int, input().split())
        ke[dau].append(cuoi)
        ke[cuoi].append(dau)
        
    #Đếm số thành phần liên thông gốc
    cntgoc = 0 
    for i in range (1, dinh + 1):
        if visited[i] ==0:
            cntgoc+=1 
            DFS(i, visited, ke)
            
    #Lần lượt xem vứt mỗi đỉnh đi thì có mấy thành phần liên thông
    res = 0 #Lưu số TPLT lớn nhất
    ans = -1 #Lưu đỉnh tạo ra nhiều TPLT nhất
    for i in range (1, dinh + 1):
        visited = [0] * 1005 #DFS xong thì phải reset lại mảng
        visited[i] = 1 #Vứt đỉnh ấy đi
        cnt = 0
        for j in range(1, dinh + 1):
            if visited[j] == 0:
                cnt += 1
                DFS(j, visited, ke)
        if cnt > cntgoc and cnt > res:
            res = cnt
            ans = i
    
    if ans == -1: print(0)
    else: print(ans)