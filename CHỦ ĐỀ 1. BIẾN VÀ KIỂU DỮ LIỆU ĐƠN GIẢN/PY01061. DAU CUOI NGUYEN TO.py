from math import *
def prime(n):
    if n<=1: return False
    for i in range (2, int(sqrt(n)) + 1):
        if n%i==0: return False
    return True
for _ in range(int(input())):
    s = input()
    x1 = int(s[:3:])
    x2 = int(s[-3::])
    if prime(x1) and prime(x2): print("YES")
    else: print("NO")