from math import *
for _ in range(int(input())):
    n = int(input())
    rev = int(str(n)[::-1])
    if gcd(n, rev) == 1: print("YES")
    else: print("NO")