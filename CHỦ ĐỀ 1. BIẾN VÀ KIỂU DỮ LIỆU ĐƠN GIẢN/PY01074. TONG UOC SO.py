min_prime = [0] * 2000005
def find_min_prime():
    for i in range(2, int(2000000**0.5) + 1):
        if min_prime[i] == 0:
            for j in range(i * i, 2000000 + 1, i):
                if min_prime[j] == 0: min_prime[j] = i
    for i in range(2, 2000001):
        if min_prime[i] == 0: min_prime[i] = i

if __name__ == "__main__":
    find_min_prime()
    t = int(input())
    res = 0
    while t > 0:
        n = int(input())
        while n != 1:
            res += min_prime[n]
            n //= min_prime[n]
        t -= 1
    print(res)
#Ghi chú: Đây là cách làm chuẩn câu này tuy nhiên không AC nổi. Muốn AC phải ... in test :))






