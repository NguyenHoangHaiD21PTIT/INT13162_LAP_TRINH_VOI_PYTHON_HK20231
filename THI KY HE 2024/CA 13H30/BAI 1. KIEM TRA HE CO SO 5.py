def check(s):
    for x in s:
        if x!="0" and x!="1" and x!="2" and x!="3" and x!="4": return False
    return True
for _ in range (int(input())):
    if check(input()): print("YES")
    else: print("NO")