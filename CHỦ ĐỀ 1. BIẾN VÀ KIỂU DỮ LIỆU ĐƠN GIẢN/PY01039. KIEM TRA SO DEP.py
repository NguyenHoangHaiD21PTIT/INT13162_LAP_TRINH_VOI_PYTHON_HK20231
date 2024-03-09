def check1(s):
    res = set()
    for x in s: res.add(x)
    if len(res) == 2: return True
    else: return False
def check2(s):
    for i in range(2, len(s)) :
        if s[i] != s[i - 2] : return False
    return True
for _ in range(int(input())):
    s = input()
    if check1(s) and check2(s): print("YES")
    else: print("NO")