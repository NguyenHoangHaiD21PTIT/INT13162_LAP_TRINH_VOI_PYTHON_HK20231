n = int(input())
a = list(map(int, input().split()))
x = int(input())
idx = []
for i in range(n):
    if a[i]==x: idx.append(str(i))
if len(idx) ==0: print("-1")
else: print(", ".join(idx))