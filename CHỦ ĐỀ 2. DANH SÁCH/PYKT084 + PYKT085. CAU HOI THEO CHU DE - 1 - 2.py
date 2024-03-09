a = [] #Lưu tên chủ đề và các câu hỏi
for _ in range(int(input())):
    s = input()
    a.append(s)
    if s == "": 
        print(a[0] + ": " + str(len(a) - 2))
        a.clear()
print(a[0] + ": " + str(len(a) - 1))