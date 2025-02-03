import sys
for line in sys.stdin:
    x = int(line.strip())
    if x == -1: break
    if x%9==0: y = 0
    else: y = 9 - x % 9 
    print(x + y)