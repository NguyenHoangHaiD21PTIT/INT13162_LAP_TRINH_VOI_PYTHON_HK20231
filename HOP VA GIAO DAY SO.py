for _ in range (int(input())):
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    c = a&b; 
    d = set()
    for x in a: d.add(x)
    for x in b: d.add(x)
    print("{:.5f}".format(len(c)/len(d)))
    