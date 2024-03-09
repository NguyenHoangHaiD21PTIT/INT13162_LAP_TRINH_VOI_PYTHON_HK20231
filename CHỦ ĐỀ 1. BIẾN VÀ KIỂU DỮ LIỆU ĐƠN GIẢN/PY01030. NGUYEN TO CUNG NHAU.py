from math import *
n, k = map(int, input().split()) #k chữ số 
cnt = 0
for i in range (int(pow(10, k - 1)), int(pow(10, k))):
    if gcd(i, n) == 1: 
        print(i, end = " ")
        cnt+=1
        if cnt == 10:
            print()
            cnt = 0