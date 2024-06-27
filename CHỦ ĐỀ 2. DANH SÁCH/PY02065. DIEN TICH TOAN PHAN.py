#Diện tích toàn phần của cột có chiều cao h nằm trong 1 ô vuông đơn vị
def area(h):
    if h == 0: return 0
    return h * 4 + 2

# Phần diện tích xung quanh chung giữa cột có chiều cao a[i][j] và cột có chiều cao h
# Chỉ xét chiều đi tức là một cột đang xét thì ta chỉ xét cột bên trái, và bên trên nó
def inter(i, j, h, arr):
    if i == 0 and j == 0: return 0
    # Hàng đầu thì chỉ bị che bởi cột bên trái
    if i == 0: return min(h, arr[i][j-1])
    # Cột đầu thì chỉ bị che bởi cột phía trên
    if j == 0: return min(h, arr[i-1][j])
    return min(h, arr[i][j-1]) + min(h, arr[i-1][j])

def calc(n, m, arr):
    ans = 0
    for i in range(n):
        for j in range(m):
            s = inter(i, j, arr[i][j], arr)
            ans += area(arr[i][j]) - s * 2
    return ans

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        a = list(map(int, input().split()))
        arr.append(a)
    print(calc(n, m, arr))
