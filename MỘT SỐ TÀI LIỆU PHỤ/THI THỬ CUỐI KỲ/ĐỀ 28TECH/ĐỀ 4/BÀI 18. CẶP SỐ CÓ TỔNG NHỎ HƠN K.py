def upper_bound(a, n, l, r, x):
    res = n
    while l <= r:
        mid = (l + r) // 2
        if a[mid] > x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    for i in range(n - 1):
        tmp = upper_bound(a, n, i + 1, n - 1, k - a[i] - 1)
        res += tmp - i - 1
    print(res)
