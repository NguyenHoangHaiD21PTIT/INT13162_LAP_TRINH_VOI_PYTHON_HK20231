n = int(input())
tong, tich = 0, 1 
for i in range(n): 
    a = input().split() 
    try:
        value = int(a[1])
        tong += value; tich *= value
    except ValueError:
        pass
if n >10: print("INVALID INPUT")
else: print(tong, tich) 