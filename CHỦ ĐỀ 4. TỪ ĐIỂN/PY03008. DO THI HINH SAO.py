n = int(input())
ke = [[] for _ in range (100005)]
for _ in range (n - 1):
    dau, cuoi = map(int, input().split())
    ke[dau].append(cuoi)
    ke[cuoi].append(dau)
a = []
for i in range (1, n + 1): a.append(len(ke[i])) #đẩy size ds kề các cạnh vào
a.sort()
if a[-1] == n-1 and a[:-1:] == [1] * (n - 1): print("Yes")
else: print("No")