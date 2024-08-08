from math import *
for _ in range (int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    kCach, vHuong = 0, 0
    for i in range(len(a)):
        vHuong+=a[i] * b[i]
        kCach+= pow(abs(a[i] - b[i]), 2)
    kCach = sqrt(kCach)
    print("{:.2f} {}".format(kCach, vHuong))
