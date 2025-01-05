n = int(input())
for _ in range(n): 
    s = input()
    s = s.lower() 
    pos = []
    for i in range(len(s)):
        if s[i]=='t': pos.append(i)
    if len(pos)==0: print(-1)
    else:
        print(pos[0], end = " ")
        if len(pos)>=1: print(pos[1], end = " ")
        print(pos[-1])