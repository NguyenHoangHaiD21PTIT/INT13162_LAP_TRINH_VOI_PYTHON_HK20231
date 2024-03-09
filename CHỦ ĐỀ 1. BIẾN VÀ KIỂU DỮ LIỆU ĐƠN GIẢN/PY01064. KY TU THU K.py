def find(n, k):
    if k == 1: return 1
    res = 2 ** (n - 1)
    if k == res: return n
    elif k < res: return find(n - 1, k)
    else: return find(n - 1, k - res)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(chr(ord('A') + find(n, k) - 1))
