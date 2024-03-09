s = input()
while len(s) > 1:
    x = str(s)[:len(s)//2:]
    y = str(s)[len(s)//2::]
    s = str(int(x) + int(y))
    print(s)

