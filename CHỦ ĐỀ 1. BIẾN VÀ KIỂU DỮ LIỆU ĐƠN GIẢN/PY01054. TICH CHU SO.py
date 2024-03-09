for _ in range(int(input())):
    s = input()
    mul = 1 
    for x in s:
        if int(x) != 0: mul*=int(x)
    print(mul)