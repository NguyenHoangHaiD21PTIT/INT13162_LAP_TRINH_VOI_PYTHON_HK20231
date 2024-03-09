n = int(input())
a = list(map(int, input().split()))
count_mod28 = [0] * 28
for x in a: count_mod28[x%28]+=1
res = 0
for i in range(1, 14): res += count_mod28[i] * count_mod28[28 - i]
res += (count_mod28[14] * (count_mod28[14] - 1)) // 2
res += (count_mod28[0] * (count_mod28[0] - 1)) // 2
print(res)