t = int(input())  
for _ in range(t):
    s = input().strip()
    s = s.replace('“', '"').replace('”', '"') 
    d = eval(s)  
    chan = []
    for k, v in d.items():
        if isinstance(v, int) and v % 2 == 0: chan.append(k)
    tong = 0
    for v in d.values():
        if isinstance(v, int): tong+= v
    cnt = 0
    for v in d.values():
        if isinstance(v, str): cnt+= 1
    print((chan, tong, cnt))
