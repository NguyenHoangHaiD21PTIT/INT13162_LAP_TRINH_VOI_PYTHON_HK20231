from math import *
for _ in range (int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    p = int(input())
    if(len(a)!=len(b)): print("INVALID")
    else:
        tong = 0
        for i in range(len(a)): tong+=pow(abs(a[i] - b[i]), p)
        tong = pow(tong, 1/p)
        print("{:.5f}".format(tong))
