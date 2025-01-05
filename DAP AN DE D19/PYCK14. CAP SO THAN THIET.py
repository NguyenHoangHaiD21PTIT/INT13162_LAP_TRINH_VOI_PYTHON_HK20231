from math import *
def tongUoc(n1):
    tong = 0
    n = n1
    for i in range (1, int(sqrt(n)) + 1):
        if n % i ==0: 
            tong+=i
            if i * i!=n: tong+=n/i 
    return tong - n1
a, b = map(int, input().split())
if a == tongUoc(b) and b == tongUoc(a): print("YES", end = "")
else: print("NO", end = "")