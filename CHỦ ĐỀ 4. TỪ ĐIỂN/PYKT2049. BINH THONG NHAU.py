par = [i for i in range(100008)]
sze = [1] * 100008

def find(x):
    if x == par[x]: return x
    par[x] = find(par[x])
    return par[x]

def Union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return False
    if sze[x] < sze[y]: x, y = y, x
    par[y] = x
    sze[x] += sze[y]
    return True

Q = int(input())
for i in range(1, 100001):
    par[i] = i
    sze[i] = 1

for _ in range(Q):
    X, Y, Z = map(int, input().split())
    if Z == 1: Union(X, Y)
    else:
        if find(X) == find(Y): print("1")
        else: print("0")
                            
            