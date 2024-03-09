file1 = open('DATA1.in', 'r')
s1 = set()
for line in file1:
    a = line.split()
    for x in a: s1.add(x.lower())
file2 = open('DATA2.in', 'r')
s2 = set()
for line in file2:
    a = line.split()
    for x in a: s2.add(x.lower())
s3 = s1 - s2
s4 = s2 - s1 
a = list(s3)
b = list(s4)
a.sort()
b.sort()
for i in a: print(i, end = " ")
print()
for i in b: print(i, end = " ")

    
