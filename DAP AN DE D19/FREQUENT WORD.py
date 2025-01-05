n = int(input())
d = dict()
for _ in range(n):
    a = list(input().split())
    for x in a:
        if x in d: d[x]+=1 
        else: d[x] = 1 
X = list(d.items())
fre = []
for x in X: 
    if x not in fre: fre.append(x[1])
fre.sort() 
kq = []
for x in X: 
    if x[1]==fre[-2]: kq.append(x[0]) 
kq.sort 
print(" ".join(kq))
'''
4
apple orange banana
banana orange fruit
mango orange
mango
'''