p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
def ma(s):
    if s>='A' and s<='Z': return ord(s) - 65
    elif s=='_': return 26
    else: return 27
while True:
    a = list(input().split())
    if a[0] == "0": break
    k = int(a[0])
    s = a[1]
    res = ""
    for x in s: res+=p[(ma(x) + k)%28]
    print(res[::-1])