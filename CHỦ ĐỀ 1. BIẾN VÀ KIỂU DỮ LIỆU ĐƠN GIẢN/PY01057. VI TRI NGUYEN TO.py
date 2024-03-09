from math import *
def prime(n):
    if n<=1: return False
    for i in range (2, int(sqrt(n)) + 1):
        if n%i==0: return False
    return True
def check(s):
    for i in range(len(s)):
        if prime(i) != prime(int(s[i])): return False
    return True
for _ in range(int(input())):
    s = input()
    if check(s): print("YES")
    else: print("NO")