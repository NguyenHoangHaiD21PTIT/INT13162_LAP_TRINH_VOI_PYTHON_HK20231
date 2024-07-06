from math import *
for _ in range(int(input())):
    n, c, d = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a, reverse= True)
    c, d = sorted([c, d])
    s1, s2 = 0, 0
    for i in a[:c]: s1+=i
    for i in a[c:c+d]: s2+=i
    print(f'{(s1/c+s2/d):.6f}')
