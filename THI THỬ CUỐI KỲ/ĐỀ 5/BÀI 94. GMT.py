h, m, a, b = map(int, input().split())
h = h - a 
if h <0: h+=24
if h >=24: h-=24
h+=b
if h <0: h+=24
if h <0: h+=24
if h >=24: h-=24
print(h, m)