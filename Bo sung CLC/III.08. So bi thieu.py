from sys import stdin, stdout
n = int(stdin.readline().strip())
a = []
for i in range(n - 1): a.append(int(stdin.readline().strip()))
b = sorted(a)
d = 1
for i in b:
    if i != d:
        print(d)
        break
    d += 1
