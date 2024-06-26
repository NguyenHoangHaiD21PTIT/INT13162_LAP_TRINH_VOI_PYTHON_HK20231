#Diện tích toàn phần của cột có chiều cao h nằm trong 1 ô vuông đơn vị
def area(h):
    if h==0: return 0
    return h*4+2
for t in range(int(input())):
    n, m = map(int, input().split())
    ans = 0
    arr = []

    #Phần diện tích xung quanh chung giữa cột có chiều cao a[i][j] và cột có chiều cao h
    #Chỉ xét chiều đi tức là một cột đang xét thì ta chỉ xét cột bên trái, và bên trên nó
    def inter(i, j, h):
        if i==0 and j==0: return 0
        #Hàng đầu thì chỉ bị che bởi cột bên trái
        if i==0: return min(h,arr[i][j-1])
        #Cột đầu thì chỉ bị che bởi cột phía trên
        if j==0: return min(h,arr[i-1][j])
        return min(h,arr[i][j-1]) + min(h,arr[i-1][j])
    
    for i in range(n):
        a = list(map(int, input().split()))
        arr.append(a)
        for j in range(m):
            s = inter(i, j, a[j])
            ans+=area(a[j])-s*2
    print(ans)
