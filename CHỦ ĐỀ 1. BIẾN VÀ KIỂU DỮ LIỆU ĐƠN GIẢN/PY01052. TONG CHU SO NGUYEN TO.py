from math import *
def prime(n):
    if n<=1: return False
    for i in range (2, int(sqrt(n)) + 1):
        if n%i==0: return False
    return True
def check(s):
    tong = 0 
    for x in s: tong+=int(x)
    if prime(tong): return True
    else: return False
for _ in range(int(input())):
    s = input()
    if check(s): print("YES")
    else: print("NO")