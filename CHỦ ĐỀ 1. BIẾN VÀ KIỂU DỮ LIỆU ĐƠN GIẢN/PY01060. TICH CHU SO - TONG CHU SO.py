for _ in range(int(input())):
    s = input()
    tong = 0 
    cnt = 0
    tich = 1
    for i in range(len(s)):
        if i% 2 ==1: tong+=int(s[i])
        else:
            if(int(s[i])!=0):
                cnt+=1 
                tich*=int(s[i])
    if cnt: print(tich, end = " ")
    else: print("0", end = " ")
    print(tong)