while True :
    n = int(input())
    if n == 0: break
    a = [] 
    for i in range(n) :
        x = int(input())
        a.append(x)
    if(min(a)==max(a)) : print("BANG NHAU")
    else : print(min(a), max(a))