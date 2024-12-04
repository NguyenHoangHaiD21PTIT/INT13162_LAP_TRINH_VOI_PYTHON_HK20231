from sys import stdin
MAXN = 100005
pos = [0] * MAXN; sum_array = [0] * MAXN; left_bound = [0] * MAXN; water = [0] * MAXN; h = [0] * MAXN
a = []
for line in stdin:
    b = list(map(int, line.strip().split()))
    for x in b: a.append(x)
t = a[0]; a.pop(0); idx = 0
for _ in range(t):
    n = a[idx]; idx += 1
    pos = [0] + a[idx:idx + n]; idx += n
    h = [0] + a[idx:idx + n]; idx += n
    for i in range(1, n + 1): sum_array[i] = sum_array[i - 1] + h[i]
    st = [0] 
    for i in range(1, n + 1):
        while st and h[st[-1]] <= h[i]: st.pop()
        if not st: left_bound[i] = 0
        else: left_bound[i] = st[-1]
        st.append(i)
    h[0] = 1000111000  
    pos[0] = -1 
    for i in range(1, n + 1):
        u = left_bound[i]
        water[i] = water[u] + (pos[i] - pos[u]) * h[i] - (sum_array[i] - sum_array[u])
    q = a[idx]; idx += 1
    for _ in range(q):
        k = a[idx]
        idx += 1
        l, r = 0, n
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if water[mid] < k:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        print(res)
