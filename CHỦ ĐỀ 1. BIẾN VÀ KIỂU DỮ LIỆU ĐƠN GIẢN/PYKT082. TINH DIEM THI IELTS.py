def band(n): #Quy đổi số câu nghe - đọc sang hệ 9
    if n == 3 or n == 4: return 2.5
    elif n == 5 or n == 6: return 3.0
    elif 7 <= n <= 9: return 3.5
    elif 10 <= n <= 12: return 4.0
    elif 13 <= n <= 15: return 4.5
    elif 16 <= n <= 19: return 5.0
    elif 20 <= n <= 22: return 5.5
    elif 23 <= n <= 26: return 6.0
    elif 27 <= n <= 29: return 6.5
    elif 30 <= n <= 32: return 7.0
    elif n == 33 or n == 34: return 7.5
    elif n == 35 or n == 36: return 8.0
    elif n == 37 or n == 38: return 8.5
    elif n == 39 or n == 40: return 9.0

def lamtron(x):
    if x == 0.25 or x == 0.375 or x == 0.625: return 0.5
    elif x == 0.75 or x == 0.875: return 1.0
    elif x == 0.125: return 0.0
    return x

t = int(input())
for _ in range(t):
    nghe, doc, noi, viet = map(float, input().split())
    tbc = (band(nghe) + band(doc) + noi + viet) / 4.0
    nguyen = int(tbc)
    le = tbc - float(nguyen)
    tbcfinal = float(nguyen) + lamtron(le)
    print("%.1f" %tbcfinal)