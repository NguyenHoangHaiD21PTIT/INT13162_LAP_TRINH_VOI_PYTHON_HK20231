f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(int(input())):
    n, k = map(int, input().split())
    s = ""
    while (n > 0):
        x = n % k
        s = f[x] + s
        n//=k
    print(s)