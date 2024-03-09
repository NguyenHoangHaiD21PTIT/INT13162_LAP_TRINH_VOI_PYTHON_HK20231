for z in range(int(input())):
    n, m, l = map(int, input().split())
    a = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1) :
        a[i] = [0] + [int(x) for x in input().split()]
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    # Xây dựng mảng cộng dồn
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + a[i][j]

    for i in range(1, n - l + 2):
        for j in range(1, m - l + 2):
            # Tính tổng cộng dồn trên HCN với hàng [i; i + l - 1] và [j; j + l - 1]
            k = (prefix[i + l - 1][j + l - 1] - prefix[i - 1][j + l - 1] - prefix[i + l - 1][j - 1] + prefix[i - 1][j - 1]) // (l * l)
            print(k, end=' ')
        print()