file = open("CONTACT.in", 'r')
s = set()
for line in file:
    x = line.strip().lower()
    s.add(x)
a = list(s)
a.sort()
for x in a: print(x)