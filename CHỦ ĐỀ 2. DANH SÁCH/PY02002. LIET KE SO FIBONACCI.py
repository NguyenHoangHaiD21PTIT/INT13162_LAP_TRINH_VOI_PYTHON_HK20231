fibo = [0] * 93
def gen():
    fibo[0] = 0
    fibo[1] = fibo[2] = 1 
    for i in range(2, 93): fibo[i] = fibo[i - 1] + fibo[i - 2]
gen()
for _ in range(int(input())):
    l, r = map(int, input().split())
    for i in range (l, r + 1): print(fibo[i], end = " ")
    print()