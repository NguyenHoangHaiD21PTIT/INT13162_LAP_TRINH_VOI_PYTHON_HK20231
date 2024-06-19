n1 = int(input())

# Bước 1: Sàng để tìm thừa số nguyên tố nhỏ nhất của mỗi số
n = int(n1**0.5)
prime = [0] * (n + 1)

for i in range(2, int(n**0.5) + 1):
    if prime[i] == 0:  # Nếu i là số nguyên tố
        for j in range(i * i, n + 1, i):  # Xét các bội của i
            if prime[j] == 0: prime[j] = i

# Gán nốt thừa số cho các số là số nguyên tố
for i in range(2, n + 1):
    if prime[i] == 0: prime[i] = i

# Bước 2: Đếm số có đúng 9 ước
cnt = 0
for i in range(2, n + 1):
    p = prime[i]
    q = prime[i // p]
    if p * q == i and p != q:  cnt += 1
    elif prime[i] == i and i**8<=n1:  cnt += 1

print(cnt)
