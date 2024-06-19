a = []
for _ in range(int(input())):
    s = input().split()
    a.append(len(s))

poem = []
i = 0
while i < len(a):
    if a[i] == 6:
        poem.append(1)
        while i < len(a) and (a[i] == 6 or a[i] == 8): i += 1
    elif a[i] == 7:
        poem.append(2)
        i += 4  

print(len(poem))
for x in poem: print(x)
