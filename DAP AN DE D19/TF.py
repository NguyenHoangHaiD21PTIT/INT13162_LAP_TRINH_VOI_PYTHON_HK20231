n = int(input())
d = {}
tong = 0 
for _ in range(n): 
    a = list(input().split())
    for x in a:
        if x in d: d[x]+=1 
        else: d[x] = 1 
    tong+=len(a) 
X = sorted(d.items(), key=lambda x: (-x[1], x[0])) 
for y in X: print(y[0], f"{(y[1]/tong):.2f}")
'''
9
hi
hi 
what is your name
my name is bond 
james bond 
my name is damme
van damme 
claude van damme 
jean claude van damme
'''