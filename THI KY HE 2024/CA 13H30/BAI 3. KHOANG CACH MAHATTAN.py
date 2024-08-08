for _ in range(int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if(len(a)!=len(b)): print("INVALID")
    else:
        tong = 0
        for i in range(len(a)): tong+=abs(a[i] - b[i])
        print("{:.5f}".format(tong))