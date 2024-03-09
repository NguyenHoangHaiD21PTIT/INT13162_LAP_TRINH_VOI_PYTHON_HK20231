from math import *
def prime(n):
    if n<=1: return False
    for i in range (2, int(sqrt(n)) + 1):
        if n%i==0: return False
    return True

def check(s):
    cnt = 0 #Đếm số lượng chữ số nguyên tố
    for x in s:
        if x == '2' or x == '3' or x == '5' or x =='7': cnt+=1 
    if cnt > len(s) - cnt: return True
    else: return False
    
for _ in range(int(input())):
    s = input()
    if prime(len(s)) and check(s): print("YES")
    else: print("NO")