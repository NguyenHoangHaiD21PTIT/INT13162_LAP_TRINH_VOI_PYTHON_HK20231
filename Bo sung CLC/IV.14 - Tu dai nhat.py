a = input().split() 
res = "" 
for x in a:
    if len(x) > len(res): res = x 
print(res, len(res))