def check(s):
    a = list(s.split("."))
    if(len(a)!=4): return False
    for x in a:
        if x.isdigit() == False: return False
        elif int(x) < 0 or int(x) > 255: return False
    return True

for _ in range(int(input())):
    s = input()
    if check(s): print("YES")
    else: print("NO")