t = int(input())
for _ in range(t):
    n = int(input())
    x, y, z = map(int, input().split())
    f = [0] * (n + 1)
    f[1] = x
    
    for i in range(2, n + 1):
        if i % 2 == 0:
            f[i] = min(f[i - 1] + x, f[i // 2] + z)
        else:
            f[i] = min(f[i - 1] + x, min(y + f[(i + 1) // 2] + z, x + f[(i - 1) // 2] + z))
    
    print(f[n])