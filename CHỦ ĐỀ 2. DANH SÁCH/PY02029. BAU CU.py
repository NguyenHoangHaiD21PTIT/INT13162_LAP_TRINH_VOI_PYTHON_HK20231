n, m = map(int, input().split())
a = list(map(int, input().split()))
d = dict()
for x in a:
    if x in d: d[x]+=1 
    else: d[x] = 1 
res = list(d.items())
res.sort(key = lambda x: (x[1], x[0]))
i = len(res) - 2
while i>=0 and res[i][1] == res[len(res) - 1][1]: i-=1 
if i==-1: print("NONE")
else: print(res[i][0])