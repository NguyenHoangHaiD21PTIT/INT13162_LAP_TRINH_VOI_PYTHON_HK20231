for _ in range (int(input())):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if len(A)!=len(B): print("INVALID")
    else:
        a, b = set(A), set(B)
        c = a&b 
        d = set()
        for x in a: d.add(x)
        for x in b: d.add(x)
        print("{:.5f}".format(len(c)/len(d)))
