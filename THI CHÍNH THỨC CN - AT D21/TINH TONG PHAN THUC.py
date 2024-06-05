for _ in range(int(input())):
    n = int(input())
    tong = 0
    if n%2:
        for i in range(1, n + 1, 2):
            if (i//2)%2==0: tong+=1/i
            else: tong-=1/i 
    else:
        for i in range(2, n + 1, 2):
            if (i//2)%2: tong+=1/i
            else: tong=1/i
    print("{:.5f}".format(tong))