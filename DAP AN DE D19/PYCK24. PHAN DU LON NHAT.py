k, m = map(int, input().split())
tong = 0 
for _ in range(k):
    a = list(map(int, input().split()))
    Max = -1 
    for x in a: Max = max(Max, (x*x)%m)
    tong+=Max 
print(tong)
