import sys
for line in sys.stdin:
    x = int(line.strip())
    if x == -1: break
    if x%11==0: print("YES")
    else: print("NO")