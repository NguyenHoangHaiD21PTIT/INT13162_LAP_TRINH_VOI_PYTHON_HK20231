from math import *
for _ in range (int(input())):
    n = input()
    tong = 0
    for x in n: tong+=factorial(int(x))
    if tong==int(n): print("Yes")
    else: print("No")