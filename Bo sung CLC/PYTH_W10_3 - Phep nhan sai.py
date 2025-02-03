import sys
def tong(s):
    res = 0
    for x in s: res += int(x)
    return res
for line in sys.stdin:
    s = line.strip()  
    if s == "-1": break
    y, z = s.split()  
    y, z = int(y), int(z)
    x = z//tong(str(y))
    print(x)