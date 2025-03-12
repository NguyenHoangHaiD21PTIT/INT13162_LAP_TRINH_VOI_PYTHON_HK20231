m, v, t, d = int(input()), int(input()), int(input()), input().strip() 
dis = v * t 
res = dis%m
if d == 'A': res = m - res 
print(res)