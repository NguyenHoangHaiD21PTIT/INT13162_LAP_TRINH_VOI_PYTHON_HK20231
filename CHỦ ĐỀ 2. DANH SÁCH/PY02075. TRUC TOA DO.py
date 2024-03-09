class DoanThang:
    def __init__(self, bd, kt):
        self.bd = bd
        self.kt = kt

for _ in range(int(input())):
    n = int(input())
    a = []
    for _ in range(n):
        s = list(map(int, input().split()))
        a.append(DoanThang(s[0], s[1]))
    a.sort(key=lambda x: x.kt)
    cnt = 1
    en = a[0].kt
    for i in range(1, n):
        if a[i].bd >= en:
            cnt += 1
            en = a[i].kt
    print(cnt)