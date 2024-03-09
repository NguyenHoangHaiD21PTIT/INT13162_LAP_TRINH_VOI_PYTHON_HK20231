import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    while len(a) < n:
        b = list(map(int, input().split()))
        for x in b: a.append(x)  
    res = int(1e9)
    check = 0  # res: Lưu chiều dài dãy con ngắn nhất  
    # TH1: Trong mảng có 1 phần tử = K thì dãy con ngắn nhất UCLN = k dài 1
    for i in range(n):
        if a[i] == k:
            check = 1
            res = 1 
    # TH2: Có thể tồn tại dãy con ngắn nhất UCLN k len >1
    if check == 0:
        for i in range(n - 1):
            tmp = a[i]
            for j in range(i + 1, n):
                tmp = math.gcd(tmp, a[j])
                if tmp == k:
                    check = 1
                    res = min(res, j - i + 1)
                    break
    if check == 0: print(-1)
    else: print(res)