n = int(input())
s = 0
a = list(map(int, input().split()))
for i in range(0, n) :
    for j in range(i + 1, n) :
        if a[i] > a[j] : s += 1
print(s)