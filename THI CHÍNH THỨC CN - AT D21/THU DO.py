t = int(input())  
for _ in range(t):
    s = input().strip()
    s = s.replace('“', '"').replace('”', '"') 
    d = eval(s)  
    x1 = []
    for k, v in d.items(): 
        if (v[0]=='a' or v[0]=='e' or v[0]=='i' or v[0]=='o' or v[0]=='u' 
        or v[0]=='A' or v[0]=='E' or v[0]=='I' or v[0]=='O' or v[0]=='U'): x1.append(k)
    cnt1 = 0
    for k, v in d.items():
        if len(k)>5: cnt1+=1 
    cnt2 = 0
    for k, v in d.items():
        if len(v)<6: cnt2+=1     
    print((x1, cnt1, cnt2))
