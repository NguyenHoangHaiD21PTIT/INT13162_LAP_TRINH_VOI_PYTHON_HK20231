s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    n, k = map(int, input().split())
    res = ""
    while(n!=0):
        res = s[n%k] + res
        n//=k 
    print(res)
    
