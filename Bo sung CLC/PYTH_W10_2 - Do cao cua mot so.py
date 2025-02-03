import sys
def tong(s):
    res = 0
    for x in s: res += int(x)
    return res
for line in sys.stdin:
    s = line.strip()  
    if s == "-1": break
    n, h = s.split()  
    n, h, cnt = int(n), int(h), 0  
    for num in range(1, n):
        if tong(str(num)) == h: cnt += 1
    print(cnt)
