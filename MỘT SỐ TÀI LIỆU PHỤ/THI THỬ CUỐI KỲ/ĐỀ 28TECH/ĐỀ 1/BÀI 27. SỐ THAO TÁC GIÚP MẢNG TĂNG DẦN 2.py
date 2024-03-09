n, d = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if a[i] <= a[i - 1]:
        chenhLech = a[i - 1] - a[i] + 1
        if chenhLech % d == 0: soThaoTac = chenhLech // d 
        else: soThaoTac = chenhLech // d + 1
        a[i]+= soThaoTac * d 
        ans+=soThaoTac
print(ans)