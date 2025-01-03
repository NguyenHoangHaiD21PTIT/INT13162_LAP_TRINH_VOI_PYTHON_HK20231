def check(a, n):
    x = a[0][0]
    for i in range(n):
        if a[i][i]!=x: return False 
    for i in range(n):
        for j in range(i + 1, n):  
            if a[i][j] != a[j][i]: return False
    return True
n = int(input())
a = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b) 
if check(a, n): print("YES")
else: print("NO")
