n = int(input())
a = list(map(int, input().split())) + [-1]
l_final, l_tmp, Max = 0, 0, max(a)
for i in range(n + 1):
    if(a[i]==Max): l_tmp+=1
    else:
        l_final = max(l_final, l_tmp)
        l_tmp = 0
print(l_final)