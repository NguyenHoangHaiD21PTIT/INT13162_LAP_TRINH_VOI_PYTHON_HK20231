from math import *
def prime(n) :
    if n < 2 : return False
    for i in range(2, int(sqrt(n)) + 1) :
        if n % i == 0: return False
    return True
m = dict()
n = int(input())
a = list(map(int, input().split()))
for i in a :
    if prime(i) == 1 :
        if i in m : m[i] += 1
        else : m[i] = 1
for i in m : print(i, m[i])

