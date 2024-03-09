d = dict()
for _ in range(10):
    s = input().split()
    d[s[0]] = int(s[1])
n = int(input())
for _ in range(n):
    s = input()
    s1 = s 
    for x in s: 
        if x.isdigit(): s = s.replace(x, " ")
    for x in s1: 
        if x.isalpha(): s1 = s1.replace(x, " ")
    a = list(s.split())
    b = list(map(int, s1.split()))
    res = 0
    for i in range(len(a)): res+=d[a[i]] * b[i]
    print(res)