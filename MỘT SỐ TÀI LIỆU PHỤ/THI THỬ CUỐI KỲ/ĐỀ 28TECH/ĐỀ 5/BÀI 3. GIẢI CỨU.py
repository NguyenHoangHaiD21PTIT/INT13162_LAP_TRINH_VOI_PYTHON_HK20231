d = dict()
a = list(input().split())
d[a[0]] = int(a[2])
b = list(input().split())
d[b[0]] = int(b[2])
status = input()

n = int(input())
for _ in range (n):
    s = list(input().split())
    if s[0] == 'witch' and status == 'ALIVE':
        if int(s[1]) >= d["POWER"]:
            d["POWER"] = 0
            d["BLOOD"] = 0
        else: d["POWER"]+=5
    elif s[0] == "mushroom" and status == 'ALIVE':
        d["POWER"]-=2
        d["BLOOD"]-=15
    elif s[0] == "pea" and status == 'ALIVE':
        d["POWER"]+=2
        d["BLOOD"]+=10
    elif s[0] == "soldier" and status == 'ALIVE':
        if int(s[1]) >= d["POWER"]:
            d["POWER"] = 0
            d["BLOOD"] = 0
        else: 
            d["POWER"]+=7
            d["BLOOD"]+=5
            
    if d["POWER"] <=0:
        d["POWER"] = 0
        status = "DEAD"
    elif d["BLOOD"] <=0:
        d["BLOOD"] = 0
        status = "DEAD"
    
    print("POWER : " + str(d["POWER"]))
    print("BLOOD : " + str(d["BLOOD"]))
    print(status)
    print("--------------------")
        