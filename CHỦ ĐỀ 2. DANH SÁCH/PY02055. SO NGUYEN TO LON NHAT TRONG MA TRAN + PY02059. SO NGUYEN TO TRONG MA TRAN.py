from math import *

def prime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True

hang, cot = map(int, input().split())
a = []
for i in range(hang):
    b = list(map(int, input().split()))
    a.append(b)

res = -1
for i in range(hang):
    for j in range(cot):
        if prime(a[i][j]): res = max(res, a[i][j])

if res == -1: print("NOT FOUND")
else:
    print(res)
    for i in range(hang):
        for j in range(cot):
            if a[i][j] == res:
                print("Vi tri [" + str(i) + "]" + "[" + str(j) + "]")