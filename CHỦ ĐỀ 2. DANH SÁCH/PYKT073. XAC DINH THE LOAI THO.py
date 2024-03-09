res = []
for _ in range (int(input())):
    a = input().split()
    res.append(len(a))
ans = []
for i in range (0, len(res) - 1):
    #Nghĩa là: Bài thơ 7 chữ đến câu thứ i là hết, sang câu thứ i + 1 là lục bát
    if res[i] == 7 and res[i + 1] == 6: ans.append(2)
    #Nghĩa là: Bài thơ lục bát đến câu thứ i là hết, sang câu thứ i + 1 là thơ 7 chữ
    elif res[i] == 8 and res[i + 1] == 7: ans.append(1)
# Xử lý câu cuối cùng
if res[-1] == 7:
    ans.append(2)
else:
    ans.append(1)
print(len(ans))
for x in ans: print(x)