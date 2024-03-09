from math import *
def prime(n):
    if n<=1: return False
    for i in range (2, int(sqrt(n)) + 1):
        if n%i==0: return False
    return True

for _ in range(int(input())):
    s = input()
    res = int(s[-4::])
    if prime(res): print("YES")
    else: print("NO")
