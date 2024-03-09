#Tính a[0]: b[0][1] = x = a[0] + a[1], b[1][2] = y = a[1] + a[2], b[0][2] = z = a[0] + a[2]
#Ta lấy (x + z - y)/2 là ra a[0]. Từ đấy xét hàng 1 ra các số còn lại
n = int(input())
b = []
for i in range(n):
    x = list(map(int, input().split()))
    b.append(x)
if n==2: print(str(b[0][1]//2) + " " + str(b[0][1]//2))
else:
    a = []
    a.append((b[0][1] + b[0][2] - b[1][2]) // 2)
    for i in range(1, n):
        a.append(b[0][i] - a[0])
    for i in range(n):
        print(a[i], end=" ")