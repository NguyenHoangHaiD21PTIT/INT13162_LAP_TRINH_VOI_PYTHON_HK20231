from math import *
def prime(n):
    if n<=1: return False
    for i in range (2, int(sqrt(n)) + 1):
        if n%i==0: return False
    return True
def check(s):
    for i in range(len(s)):
        if i%2 != int(s[i]) % 2: return False
    return True
for _ in range(int(input())):
    s = input()
    tong = 0
    for x in s: tong+=int(x)
    if check(s) and prime(tong): print("YES")
    else: print("NO")