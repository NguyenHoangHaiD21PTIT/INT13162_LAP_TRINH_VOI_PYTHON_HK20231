from math import *
n = int(input())
a = list(map(float, input().split()))
Min = min(a)
Max = max(a)
ans = []
for x in a: 
    if x!=Min and x!=Max: ans.append(x)
p = sum(ans)/len(ans)
print("%.2f" %p)
