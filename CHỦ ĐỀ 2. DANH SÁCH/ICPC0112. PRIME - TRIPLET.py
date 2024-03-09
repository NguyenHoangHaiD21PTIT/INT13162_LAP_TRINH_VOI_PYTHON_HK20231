prime = [1] * 1000001
def sang():
    prime[0] = prime[1] = 0 
    for i in range (2, 1001):
        if prime[i]:
            for j in range (i*i, 1000001, i): prime[j] = 0
sang()

for _ in range(int(input())):
    n = int(input())
    s = 0
    for i in range(6, n):
        if prime[i] == 1 and prime[i - 6] == 1 and (prime[i - 2] == 1 or prime[i - 4] == 1): s += 1
    print(s)