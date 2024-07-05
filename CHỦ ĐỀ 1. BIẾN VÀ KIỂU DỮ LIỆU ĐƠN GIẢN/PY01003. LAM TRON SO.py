for _ in range(int(input())):
    s = input()
    a = []
    for x in s: a.append(int(x))
    for i in range(len(a) - 1, 0, -1):
        if a[i] >= 5: a[i - 1] += 1
        a[i] = 0
    for x in a: print(x, end = "")
    print()
