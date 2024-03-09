from math import *

def check(n):
    if len(str(n)) < 2: return False
    elif str(n) != str(n)[::-1]: return False
    else: return True

hang, cot = map(int, input().split())
a = []
for i in range(hang):
    b = list(map(int, input().split()))
    a.append(b)

res = -1
for i in range(hang):
    for j in range(cot):
        if check(a[i][j]): res = max(res, a[i][j])

if res == -1: print("NOT FOUND")
else:
    print(res)
    for i in range(hang):
        for j in range(cot):
            if a[i][j] == res:
                print("Vi tri [" + str(i) + "]" + "[" + str(j) + "]")