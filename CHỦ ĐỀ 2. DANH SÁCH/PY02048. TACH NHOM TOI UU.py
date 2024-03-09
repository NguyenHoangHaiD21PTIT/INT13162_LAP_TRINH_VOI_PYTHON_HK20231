n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = 1
for i in range(1, n) :
    if a[i] - a[i - 1] > k: s += 1
print(s)