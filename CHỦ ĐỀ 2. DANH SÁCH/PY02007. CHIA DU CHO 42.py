from sys import stdin 
res = set()
for line in stdin:
    a = list(map(int, line.split()))
    for i in a: res.add(i%42)
print(len(res))
    