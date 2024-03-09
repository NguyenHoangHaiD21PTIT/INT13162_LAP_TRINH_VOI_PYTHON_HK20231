def check(s):
    tong = 0 #Đếm số lượng chữ số nguyên tố
    for x in s: tong+=int(x)
    res = str(tong)
    if len(res) > 1 and res == res[::-1]: return True
    else: return False
for _ in range(int(input())):
    s = input()
    if check(s): print("YES")
    else: print("NO")