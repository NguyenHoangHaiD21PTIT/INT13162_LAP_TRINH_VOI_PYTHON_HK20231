from math import *

for _ in range(int(input())):
    p, q = map(int, input().split())
    x = min(p, q)
    y = max(p, q)

    a = list(input().split())
    if len(a) == 2:
        x1 = a[0]
        x2 = a[1]
    else:
        x1 = a[0]
        x2 = input()
    minx1 = x1.replace(str(y), str(x))
    minx2 = x2.replace(str(y), str(x))
    
    maxx1 = x1.replace(str(x), str(y))
    maxx2 = x2.replace(str(x), str(y))

    print(int(minx1) + int(minx2), int(maxx1) + int(maxx2), sep=" ")
#Bài này x1, x2 có thể nằm trên cùng 1 dòng, thậm chí thừa dấu cách