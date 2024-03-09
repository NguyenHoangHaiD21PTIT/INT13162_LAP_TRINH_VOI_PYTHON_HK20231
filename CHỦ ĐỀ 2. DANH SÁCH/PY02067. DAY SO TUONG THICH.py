def check(p):
    for i in a:
        if i//p < i//(p + 1) + 1: return 0
    return 1
n = int(input())
a = list(map(int, input().split()))
s, ans = min(a), 0
for i in range(s, 0, -1) :#Tìm số p max thỏa mãn. Tức là xét từng số i từ min mảng
    if check(i) :#Số p max thỏa mãn
        for j in range(n) : ans += a[j]//(i+1)+ 1
        break
print(ans)