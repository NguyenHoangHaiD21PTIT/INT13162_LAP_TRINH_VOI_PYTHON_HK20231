def check(a):
    for i in a:
        if i != '4' and i != '7' : return False
    return True
for i in range(int(input())):
    s = input()
    if check(s) == True : print("YES")
    else : print("NO")