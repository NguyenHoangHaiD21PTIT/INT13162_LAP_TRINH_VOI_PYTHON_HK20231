prime = [1] * 1000001
def sang():
    prime[0] = prime[1] = 0 
    for i in range (2, 1001):
        if prime[i]:
            for j in range (i*i, 1000001, i): prime[j] = 0
sang()

for _ in range(int(input())):
    n = int(input())
    for i in range (13, n):
        rev = int(str(i)[::-1])
        #Trong mỗi cặp số bắt buộc i nhỏ hơn rev, in i trước rev sau
        if rev > i and rev < n and prime[rev] and prime[i]: print(i, rev, sep = " ", end =" ")
    print()