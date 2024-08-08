for _ in range(int(input())):
    s = input()
    tong = 0 
    tich = 1
    for i in range(len(s)):
        if i% 2: tong+=int(s[i])
        else:
            if(int(s[i])!=0): tich*=int(s[i])
    if tong==0: print("INVALID")
    else: print("{:.6f}".format(tich/tong))
    