prime = [1] * 10000
def sang():
    prime[0] = prime[1] = 0 
    for i in range (2, 100):
        if prime[i]:
            for j in range (i*i, 10000, i): prime[j] = 0
sang()
a = []
for i in range(2, 10000):
    if prime[i]: a.append(i)
n, x = map(int, input().split())
print(x, end = " ")
for i in range(0, n): 
    x+=a[i]
    print(x, end =" ")



