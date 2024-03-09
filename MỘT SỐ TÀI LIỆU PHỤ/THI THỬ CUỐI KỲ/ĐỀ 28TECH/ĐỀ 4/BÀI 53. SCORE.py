from sys import stdin
d = dict()
res = []
for line in stdin:
    s = line.split("-")
    a = s[0].split()
    b = s[1].split()
    doia = ""; diema = 0; doib = ""; diemb = 0;
    for i in range(0, len(a) - 1): doia+=a[i] + " "
    doia = doia.strip()
    diema = int(a[-1].strip())
    for i in range(1, len(b)): doib+=b[i] + " "
    doib = doib.strip()
    diemb = int(b[0].strip())
    if doia in d: 
        d[doia]+=diema
    else: 
        d[doia] = diema
        res.append(doia)
    if doib in d: 
        d[doib]+=diemb
    else: 
        d[doib] = diemb
        res.append(doib)
res.sort(key = lambda x: (-d[x], x))
for x in res: print(x + " " + str(d[x]))