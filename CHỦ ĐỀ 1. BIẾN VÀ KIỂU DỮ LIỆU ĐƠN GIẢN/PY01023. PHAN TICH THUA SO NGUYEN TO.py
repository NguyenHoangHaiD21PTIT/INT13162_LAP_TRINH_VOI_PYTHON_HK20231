from math import *
def ptich(n):
    s = "1 * "
    for i in range(2, int(sqrt(n)) + 1):
        if n%i ==0:
            cnt = 0
            while n%i ==0:
                cnt+=1
                n//=i
            s = s + str(i) + "^" + str(cnt) + " * "
    if n!=1: s = s + str(n) + "^" + "1"
    if s[-2] =='*': s = s[:- 2:]
    return s
for _ in range(int(input())):
    n = int(input())
    s = ptich(n)
    print(s)