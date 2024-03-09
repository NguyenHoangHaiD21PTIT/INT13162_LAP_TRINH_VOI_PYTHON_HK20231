from math import *
for _ in range (int(input())):
    n = int(input())
    n*=2
    cnt = 0
    for i in range (2, int(sqrt(n)) + 1):
        if n % i == 0:
            r = i + n //i - 1
            if r % 2 == 0:
                r //=2
                l = n //i - r
                if l >=1 and l < r: cnt += 1 
    print(cnt)