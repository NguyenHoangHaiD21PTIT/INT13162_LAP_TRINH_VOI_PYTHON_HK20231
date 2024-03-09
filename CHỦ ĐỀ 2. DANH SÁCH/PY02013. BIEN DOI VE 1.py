while True:
    n = int(input())
    if n == 0: break
    result = []
    result.append(1)
    while n != 1:
        if n % 2 == 0: n = n/2
        else: n = n*3 + 1
        result.append(n)
    print(len(result))