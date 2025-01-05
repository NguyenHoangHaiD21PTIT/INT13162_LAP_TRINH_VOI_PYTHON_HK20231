def solve(s):
    x = ".,? "
    for y in x: s = s.replace(y, '')
    s = s.lower() 
    return s
a, b = input(), input() 
a = solve(a); b = solve(b)
x, y = set(), set()
for a1 in a: x.add(a1)
for b1 in b: y.add(b1)
hop = x | y
giao = x & y 
j = len(giao)/len(hop) 
print(f"{j:.2f}")
