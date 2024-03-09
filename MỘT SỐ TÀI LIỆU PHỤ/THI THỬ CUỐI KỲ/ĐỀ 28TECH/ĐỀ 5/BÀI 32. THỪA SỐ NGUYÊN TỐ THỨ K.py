from math import *
def uocnt(n, k):
    dem = 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i ==0:
            while n % i == 0:
                dem+=1
                n//=i
                if dem == k: return i
    if n!=1: dem+=1
    if dem==k: return n
    else: return -1

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(uocnt(n, k))