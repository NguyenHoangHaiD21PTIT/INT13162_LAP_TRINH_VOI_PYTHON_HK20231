from math import *
prime = [1] * 1300000
def sang():
    prime[0] = prime[1] = 0 
    for i in range (2, int(sqrt(1300000)) + 1):
        if prime[i]:
            for j in range (i*i, 1300000, i): prime[j] = 0
sang()
a = []
for i in range (1300000):
    if prime[i]: a.append(i)
l, r = map(int, input().split())
p = input()
res = 0
for i in range (l, r + 1):
    if str(a[i - 1]).count(p): res+=1
print(res)