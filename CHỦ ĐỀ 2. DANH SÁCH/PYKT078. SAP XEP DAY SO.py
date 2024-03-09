for _ in range (int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    Max = max(a)
    #Bước 1: Chèn m vào vị trí đầu tiên = GTLN
    for i in range(n) :
        if a[i] == Max :
            a.insert(i, m)
            break
    b, c = [], []
    for i in a :
        if i < 0 : b.append(i)
        else : c.append(i)
    for i in b : print(i, end = " ")
    for i in c : print(i, end = " ")
    print()