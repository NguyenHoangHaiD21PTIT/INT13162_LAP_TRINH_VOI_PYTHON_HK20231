from math import *
def prime(n):
    if n<=1: return False
    for i in range (2, int(sqrt(n)) + 1):
        if n% i==0: return False
    return True
hang, cot = map(int, input().split())
a = []
for i in range (hang):
    b = list(map(int, input().split()))
    a.append(b)
for i in range (hang):
    for j in range (cot):
        if prime(a[i][j]): print("1", end = " ")
        else: print("0", end = " ")
    print()