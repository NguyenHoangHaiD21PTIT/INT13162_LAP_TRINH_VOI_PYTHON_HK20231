def checktang(s):
    for i in range (len(s) - 1):
        if s[i] >= s[i + 1]: return False
    return True
def checkgiam(s):
    for i in range (len(s) - 1):
        if s[i] <= s[i + 1]: return False
    return True
def check(s):
    if len(s) <3: return False
    for i in range (1, len(s) -1):
        x1 = s[:i+1:]
        x2 = s[i::]
        if checktang(x1) and checkgiam(x2): return True 
    return False
for _ in range (int(input())):
    s = input()
    if check(s): print("YES")
    else: print("NO")