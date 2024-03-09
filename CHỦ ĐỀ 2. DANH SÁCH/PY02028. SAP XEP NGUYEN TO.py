from sys import stdin
from math import *

def prime(n):
    if n<=1: return False
    for i in range (2, int(sqrt(n)) + 1):
        if n % i ==0 : return False
    return True

n = int(input())
a = []
d = [0] * n #d[i] = 1 tức là vị trí i là số nguyên tố và ngược lại
nto = []
knto = []

for line in stdin:
    x = list(map(int, line.split()))
    for i in x: a.append(i)
    
#Phân loại số nguyên tố, không nguyên tố và đánh dấu đâu là vị trí chứa SNT
for i in range (n):
    if prime(a[i]):
        nto.append(a[i])
        d[i] = 1 
    else: knto.append(a[i])
    
#Sắp xếp DS các SNT giảm dần, đảo ngược list các số kp SNT
nto.sort(reverse = True)
knto = knto[::-1]

for i in range (n):
    if d[i] == 1: #Với vị trí chứa số nguyên tố, lần lượt in số bé nhất, tức đỉnh list, in xong xóa
        print (str(nto[-1]), end = " ")
        nto.pop()
    else: 
        print(str(knto[-1]), end = " ")
        knto.pop()