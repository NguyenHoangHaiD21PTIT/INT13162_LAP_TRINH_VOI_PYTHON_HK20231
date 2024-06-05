for _ in range(int(input())):
    s = input()
    s+="x"
    ans, dem = 0, 0
    for x in s:
        if x=='0': dem+=1
        else:
            ans = max(ans, dem)
            dem = 0 
    print(ans)