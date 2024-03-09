from itertools import combinations
n1, k = map(int, input().split())
s = set(map(int,input().split()))
a = list(s)
a.sort()
n = len(a)
comb = combinations(a, k) #Sinh các tổ hợp chập k của list n
for c in comb:
    for j in c: print(j, end = " ")
    print()
