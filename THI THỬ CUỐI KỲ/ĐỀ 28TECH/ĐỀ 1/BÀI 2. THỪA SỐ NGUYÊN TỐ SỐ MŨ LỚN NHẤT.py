from math import *
n = int(input())
d = dict()
for i in range (2, int(sqrt(n)) + 1):
    if n % i ==0:
        cnt = 0
        while n % i ==0:
            cnt+=1
            n//=i 
        d[i] = cnt 
if n!=1: d[n] = 1
a = list(d.items())
a.sort(key = lambda x: (-x[1], x[0]))
print(a[0][0], a[0][1], end = " ")