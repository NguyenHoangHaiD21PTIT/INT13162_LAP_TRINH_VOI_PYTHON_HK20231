MAX = 1000000
MOD = 1000000007
prime = [1] * (MAX + 1)
primes = []

def sieve():
    prime[0], prime[1] = 0, 0
    for i in range(2, int(MAX**0.5) + 1):
        if prime[i] == 1:
            for j in range(i * i, MAX + 1, i): prime[j] = 0
    for i in range(2, MAX + 1):
        if prime[i] == 1: primes.append(i)

def count_factors(n, p):
    count = 0
    while n >= p:
        count += n // p
        n //= p
    return count

sieve()
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ans = 1
    for x in primes:
        if x > b:
            break
        d1 = count_factors(b, x)
        d2 = count_factors(a - 1, x)
        ans = ans * (2 * (d1 - d2) + 1) % MOD
    print(ans)
