s = input()
if len(s) % 2: s = s[:-1:]
a = []
for i in range(0, len(s) - 1, 2): a.append(int(s[i:i+2]))
cnt = [0] * 100
for x in a: cnt[x]+=1 
for x in a:
    if cnt[x]:
        print(x, end = " ")
        cnt[x] = 0



