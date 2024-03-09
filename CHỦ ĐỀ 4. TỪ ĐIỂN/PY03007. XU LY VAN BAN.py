from sys import stdin
s = ""
for line in stdin:
    a = line.strip().split()
    for x in a: s+= x + " "
s = s.lower()
s = s.replace('?', '.')
s = s.replace('!', '.')
s = s.replace(". ", ".")
s = s.replace(" . ", ".")
s = s.replace(" .", ".")
res = s.split(".")
for tmp in res: print(tmp.capitalize())