n, m = map(int, input().split())
a = list(map(int, input().split()))
s = set()
for x in a: s.add(x)
s.add(m)
cnt = 1
b = list(s)
b.sort()
for x in b:
    if x == m:
        print(cnt)
        break
    cnt+=1