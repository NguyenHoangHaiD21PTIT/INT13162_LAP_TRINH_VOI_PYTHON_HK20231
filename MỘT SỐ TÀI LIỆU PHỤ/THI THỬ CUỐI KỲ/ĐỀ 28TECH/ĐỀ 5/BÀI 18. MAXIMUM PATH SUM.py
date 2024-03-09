from math import *
a = []
hang, cot = map(int, input().split())
for i in range (hang):
    b = list(map(int, input().split()))
    a.append(b)
for i in range (hang):
    for j in range (cot):
        if i == 0 and j !=0: a[i][j]+=a[i][j - 1]
        elif i != 0 and j ==0: a[i][j]+=a[i - 1][j]
        elif i != 0 and j !=0: a[i][j]+=max(a[i-1][j], a[i][j-1], a[i-1][j-1])
print(a[hang - 1][cot - 1])