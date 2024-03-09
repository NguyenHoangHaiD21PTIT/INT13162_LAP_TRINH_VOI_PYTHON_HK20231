for _ in range(int(input())):
    s = input()
    for x in s:
        if x.isalpha(): s = s.replace(x, ' ')
    a = list(map(int, s.split()))
    print(max(a))
