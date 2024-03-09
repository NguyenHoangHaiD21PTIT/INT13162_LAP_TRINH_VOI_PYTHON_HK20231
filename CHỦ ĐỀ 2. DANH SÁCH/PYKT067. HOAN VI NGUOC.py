from math import *
from itertools import permutations
for _ in range (int(input())):
    n = int(input())
    a = []
    for i in range (1, n + 1): a.append(i)
    print(factorial(n))
    res = permutations(a)
    res1 = list(res)[::-1]
    for x in res1:
        for i in x: print(i, end = "")
        print(" ", end = "")
    print()
    