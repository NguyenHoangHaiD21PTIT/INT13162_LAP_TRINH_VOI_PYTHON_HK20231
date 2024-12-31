from math import *
for _ in range (int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if(len(a)!=len(b)): print("INVALID")
    else:
        tong = 0
        for i in range(len(a)): tong+=pow(a[i] - b[i], 2)
        tong = sqrt(tong)
        print("{:.5f}".format(tong))