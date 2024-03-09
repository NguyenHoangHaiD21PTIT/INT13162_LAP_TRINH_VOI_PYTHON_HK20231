for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l = min(a)
    r = max(a)
    res = set(a)
    print(r - l + 1 - len(res))
            