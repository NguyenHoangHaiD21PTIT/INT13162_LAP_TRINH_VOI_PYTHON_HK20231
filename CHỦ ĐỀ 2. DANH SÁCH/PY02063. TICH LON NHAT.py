n = int(input())
a = list(map(int, input().split()))

a.sort()
x1 = a[0] * a[1]
x2 = a[-2] * a[-1]
x3 = x2 * a[-3]
x4 = a[0] * a[1] * a[-1]
ans = max(x1, max(x2, max(x3, x4)))
print(ans)