n = int(input())
s = 0
a = list(map(int, input().split()))
for i in range(1, n) :
    if a[i] != a[i - 1] : s += 1
print(s)

