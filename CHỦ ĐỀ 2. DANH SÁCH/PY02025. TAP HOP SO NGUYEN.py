m, n = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = a&b
giao = list(c)
giao.sort()
for i in giao: print(i, end = " ")
print()

d = a - b
hieu1 = list(d)
hieu1.sort()
for i in hieu1: print(i, end = " ")
print()

e = b - a
hieu2 = list(e)
hieu2.sort()
for i in hieu2: print(i, end = " ")