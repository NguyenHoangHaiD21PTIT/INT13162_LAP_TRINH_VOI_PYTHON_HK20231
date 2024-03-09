from math import *

hang, cot = map(int, input().split())
a = []
for i in range(hang):
    b = list(map(int, input().split()))
    a.append(b)

Min = 20000
Max = -1
for i in range(hang):
    for j in range(cot):
        Min = min(Min, a[i][j])
        Max = max(Max, a[i][j])

res = Max - Min
check = 0
for i in range(hang):
    for j in range(cot):
        if a[i][j] == res:
            check=1
            break
if check:
    print(res)
    for i in range(hang):
        for j in range(cot):
            if a[i][j] == res:
                print("Vi tri [" + str(i) + "]" + "[" + str(j) + "]")
else: print("NOT FOUND")