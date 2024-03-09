s = input()
hoa, thuong = 0, 0
for x in s:
    if x.isupper(): hoa+=1 
    else: thuong+=1 
if hoa > thuong: print(s.upper())
else: print(s.lower())