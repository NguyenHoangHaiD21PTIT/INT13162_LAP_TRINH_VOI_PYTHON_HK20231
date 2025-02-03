h0, m0, s0 = map(int, input().split())  
h1, m1, s1 = map(int, input().split()) 
if h1 < h0: h1 += 24  
res = (h1 * 3600 + m1 * 60 + s1) - (h0 * 3600 + m0 * 60 + s0)
print(res)
