s1 = input()
s2 = input()
s3, s4 = s1.lower(), s2.lower()
a1 = set(s3.split())
a2 = set(s4.split())
giao = a1&a2
hop = a1|a2
res1 = list(giao)
res2 = list(hop)
res2.sort()
for i in res2: print(i, end = " ")
print()
res1.sort()
for i in res1: print(i, end = " ")