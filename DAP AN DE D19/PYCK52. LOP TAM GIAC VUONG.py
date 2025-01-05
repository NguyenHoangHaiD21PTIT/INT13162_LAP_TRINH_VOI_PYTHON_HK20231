a = list(map(int, input().split()))
a.sort()
if a[0]**2 + a[1]**2 == a[2] **2: 
    dienTich = a[0] * a[1]//2 
    chuVi = a[0] + a[1] + a[2]
    print(chuVi, dienTich)
else: print("INVALID")