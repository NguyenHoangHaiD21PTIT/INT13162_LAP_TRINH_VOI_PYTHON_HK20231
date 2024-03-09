def solve(s):
    res = ""
    a = s.split()
    for x in a: res+=x + " "
    res = res.strip()
    res = res.replace(' ?', '?')
    res = res.replace(' .', '.')
    res = res.replace(' !', '!')
    if not res.endswith(('.', '!', '?')): res += '.'
    return res.capitalize().strip()
from sys import stdin
s = ""
for line in stdin: print(solve(line))