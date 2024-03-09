for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    res = 0
    for x in s: res ^= x
    print(res)