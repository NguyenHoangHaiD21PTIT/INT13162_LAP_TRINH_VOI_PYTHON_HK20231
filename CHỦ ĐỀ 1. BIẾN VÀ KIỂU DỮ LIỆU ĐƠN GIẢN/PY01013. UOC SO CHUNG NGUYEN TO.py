from math import *
def prime(n):
    if n<=1: return False
    for i in range (2, int(sqrt(n)) + 1):
        if n % i==0: return False
    return True
for _ in range(int(input())):
    a, b = map(int, input().split())
    res = gcd(a, b)
    kq = str(res)
    tong = 0 
    for x in kq: tong+=int(x)
    if prime(tong): print("YES")
    else: print("NO")