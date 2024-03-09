from math import *
a, K, N = map(int, input().split())
if a/K == ceil(a/K): Min = ceil(a/K) + 1
else: Min = ceil(a/K)
Max = floor(N/K)
if(Min > Max): print("-1")
else:
    for i in range(Min, Max + 1): print(i * K - a, end = " ")