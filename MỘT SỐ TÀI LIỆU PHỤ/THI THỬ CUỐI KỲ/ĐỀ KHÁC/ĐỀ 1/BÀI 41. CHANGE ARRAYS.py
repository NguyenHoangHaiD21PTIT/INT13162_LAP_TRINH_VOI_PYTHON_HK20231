n, k = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
for i in range(n):
    if a[i] < 0 and k > 0:
        a[i] = -a[i]
        k-=1
a = sorted(a)
if k%2==1: a[0] = -a[0]
print(sum(a))