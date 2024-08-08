for _ in range(int(input())):
    a = list(input().split())
    b = list(input().split())
    s1= set()
    for x in a: s1.add(x.lower()) #Lưu các từ in thường phân biệt của A
    res = []
    for x in b: 
        if x.lower() in s1: print(x, end = " ") 