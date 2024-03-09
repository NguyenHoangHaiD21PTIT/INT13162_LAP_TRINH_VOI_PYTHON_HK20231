a = input().strip().split()
for x in a: 
    print(x[0].upper() + x[1::], end = "")