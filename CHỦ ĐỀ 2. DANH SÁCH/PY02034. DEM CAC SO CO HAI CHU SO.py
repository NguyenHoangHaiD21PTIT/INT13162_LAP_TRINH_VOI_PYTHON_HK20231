from collections import Counter
s = input()
if len(s) % 2: s = s[:-1:]
a = []
for i in range(0, len(s) - 1, 2): a.append(int(s[i:i+2]))
b = Counter(a)
for x, y in b.items(): print(x, y)



