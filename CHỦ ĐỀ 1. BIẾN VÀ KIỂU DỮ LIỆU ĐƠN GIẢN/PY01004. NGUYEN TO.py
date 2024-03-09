from math import *
prime = [1] * 1000001
def sang():
    prime[0] = prime[1] = 0 
    for i in range (2, 1001):
        if prime[i]:
            for j in range (i*i, 1000001, i): prime[j] = 0
sang()
for _ in range(int(input())):
    n = int(input())
    res = 0
    for i in range (1, n):
        if gcd(i, n) == 1: res+=1
    if prime[res]: print("YES")
    else: print("NO")