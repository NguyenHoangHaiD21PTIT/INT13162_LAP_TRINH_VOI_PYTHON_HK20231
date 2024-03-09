for i in range (int(input())):
    a = list(input())
    b = list(input())
    print("Test " + str(i + 1) + ": ", end = "")
    a.sort()
    b.sort()
    if a == b: print("YES")
    else: print("NO")
