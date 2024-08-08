def check(s):
    if len(s)%2: return "NO"
    if s[0]==s[2]: return "NO"
    for i in range(1, len(s) - 2, 2):
        if s[i]!=s[i + 2]: return "NO"
    return "YES"
#01234567
for _ in range(int(input())):
    s = input()
    print(check(s))
