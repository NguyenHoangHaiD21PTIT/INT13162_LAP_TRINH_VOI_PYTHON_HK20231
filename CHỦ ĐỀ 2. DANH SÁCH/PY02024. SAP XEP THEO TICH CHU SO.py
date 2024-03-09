from functools import cmp_to_key
def tich(n):
    res = 1
    for x in str(n): res*=int(x)
    return res
for _ in range (int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = lambda x: (tich(x), x))
    for x in a: print(x, end = " ")
    print()
