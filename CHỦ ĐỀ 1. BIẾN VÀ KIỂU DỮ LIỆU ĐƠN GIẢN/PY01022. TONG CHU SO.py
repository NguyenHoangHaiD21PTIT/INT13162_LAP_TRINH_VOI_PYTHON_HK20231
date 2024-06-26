s = input()
cnt = 0
if len(s)==1:  print(1)
else: 
    while len(s)>1:
        tong = 0
        for x in s: tong+=ord(x) - 48
        s = str(tong)
        cnt+=1 
    print(cnt)