from collections import Counter
s = input()
if len(s) % 2: s = s[:-1:]
k = int(input())
a = []
for i in range(0, len(s) - 1, 2): a.append(int(s[i:i+2]))
b = Counter(a)
c = dict(b)
d = list(c.items())
d.sort(key = lambda x: (x[0]))
check = 0
for x in d:
    if x[1] >= k: 
        check = 1 
        print(x[0], x[1])
if check == 0: print("NOT FOUND")

