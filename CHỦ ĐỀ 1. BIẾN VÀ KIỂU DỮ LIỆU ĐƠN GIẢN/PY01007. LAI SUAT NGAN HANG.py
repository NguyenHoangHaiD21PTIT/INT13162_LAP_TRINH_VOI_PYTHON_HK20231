from math import *
for _ in range (int(input())):
    n, x, m = map(float, input().split())
    res = ceil(log(m/n, 1.0 + x/100))
    print(res)
