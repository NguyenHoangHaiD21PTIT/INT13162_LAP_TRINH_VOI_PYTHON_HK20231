for _ in range(int(input())):
    s, k = input().strip().split()
    k = int(k)
    ans = ""
    for x in s:
        if x.isupper(): base = ord('A')
        else: base = ord('a')
        x = chr((ord(x) - base + k) % 26 + base)
        ans+=x 
    print(ans)
