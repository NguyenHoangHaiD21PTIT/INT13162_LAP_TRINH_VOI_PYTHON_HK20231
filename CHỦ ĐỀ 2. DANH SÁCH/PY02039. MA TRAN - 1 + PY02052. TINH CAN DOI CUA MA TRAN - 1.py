from math import *
n = int(input())
a = []
for i in range (n):
    b = list(map(int, input().split()))
    a.append(b)
k = int(input())
tongtren = 0
tongduoi = 0
for i in range (n):
    for j in range (n):
        if i < j: tongtren+=a[i][j]
        elif i > j: tongduoi+=a[i][j]
if abs(tongtren - tongduoi) <=k : print("YES")
else: print("NO")
print(abs(tongtren - tongduoi))



