from math import *
t = int(input())
for _ in range(t): 
    n, p, x = map(float, input().split())
    q = 1 - p 
    kq = comb(int(n), int(x)) * pow(p, x) * pow(q, n - x)
    print(kq)