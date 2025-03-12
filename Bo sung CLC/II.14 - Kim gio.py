h, m, s = map(int, input().split()) 
res = h * 30 + m * 0.5 + s * (0.5 / 60)
print('Angle:', res)