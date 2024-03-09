p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def ma(s):
    return ord(s) - 65

def rotate(s):
    tmp = 0
    for x in s: tmp += ma(x)
    res = ""
    for x in s: res += p[(ma(x) + tmp) % 26]
    return res

def drm(s1, s2):
    n = len(s1)
    res = ""
    for i in range(n): res += p[(ma(s1[i]) + ma(s2[i])) % 26]
    return res

for _ in range(int(input())):
    s = input()
    n = len(s) // 2
    
    # Bước 1: Chia đôi
    s1 = s[:n]
    s2 = s[n:]
    
    # Bước 2: Xoay xâu
    s1 = rotate(s1)
    s2 = rotate(s2)
    
    # Bước 3: Tìm xâu DRM
    print(drm(s1, s2))
