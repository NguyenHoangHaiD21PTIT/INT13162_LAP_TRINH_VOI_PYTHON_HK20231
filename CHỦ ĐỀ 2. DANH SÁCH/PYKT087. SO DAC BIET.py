MOD = 10**9 + 7
def powdu(a, b):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return res
def dec_to_bin(n):
    return str(bin(n))[2::]
for _ in range(int(input())):
    n, k = map(int, input().split())
    tong = 0 
    s = dec_to_bin(k)
    for i in range(len(s)):
        if(s[i]=='1'): 
            tong+=powdu(n, len(s) - i - 1)
            tong%=MOD 
    print(tong)