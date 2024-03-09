from math import *
def prime(n):
    if n<=1: return False
    for i in range (2, int(sqrt(n)) + 1):
        if n % i==0: return False
    return True
def checkstr(s):
    for x in s:
        if x!='2' and x!='3' and x!='5' and x!='7': return False
    return True
def checksumdigit(s):
    tong = 0
    for x in s: tong+=int(x)
    if prime(tong): return True
    else: return False
for _ in range(int(input())):
    n = int(input())
    rev = int(str(n)[::-1])
    if prime(n) and prime(rev) and checksumdigit(str(n)) and checkstr(str(n)): print("Yes")
    else: print("No")