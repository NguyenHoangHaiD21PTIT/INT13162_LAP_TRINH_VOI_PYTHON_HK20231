from math import *
n, x = map(int, input().split())
cnt = 0
for i in range(1, int(sqrt(x)) + 1):
    if x % i == 0:
        if i <=n and x//i<=n:
            if i != x//i: cnt+=2
            else: cnt+=1 
    if i > n: break
print(cnt)