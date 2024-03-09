def powdu(a, b, MOD):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return res
a, b, y = map(int, input().split())
print(powdu(a, b, 10 ** y))