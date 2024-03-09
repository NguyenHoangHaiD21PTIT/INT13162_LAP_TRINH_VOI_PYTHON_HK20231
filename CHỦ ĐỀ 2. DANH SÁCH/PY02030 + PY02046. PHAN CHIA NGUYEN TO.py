from math import *

#Kiểm tra nguyên tố
def prime(n):
    if n<=1: return False
    for i in range (2, int(sqrt(n)) + 1):
        if n% i==0: return False
    return True

#Xử lý trùng nhau    
n1 = int(input())
a = list(map(int, input().split()))
s = set() 
b = []
for x in a:
    if x not in s: b.append(x) 
    s.add(x)
n = len(s)
#Xây dựng mảng cộng dồn
pre = [0] * n
pre[0] = b[0]
for i in range (1, n): pre[i] = pre[i - 1] + b[i]
check = False

#Kiểm tra tổng cộng dồn
for i in range (0, n - 1):
    if prime(pre[i]) == True and prime(pre[n - 1] - pre[i]) == True:
        check = True
        print(i)
        break
if check == False: print("NOT FOUND")

