n, a = int(input()), list(map(int, input().split()))
s, ans = set(), set()
for i in a:
    new_set = set()
    for j in s: 
        new_set.add(i|j)
        ans.add(i|j)
    ans.add(i)
    new_set.add(i)
    s = new_set
print(len(ans))
'''
VD: a0 a1 a2 a3 
S = {a0, a0|a1, a1, a0|a1|a2, a1|a2, a2, a0|a1|a2|a3, a1|a2|a3, a2|a3, a3}
ans: Tập S
Khi xét đến index i:
s BAN ĐẦU: Tập các dãy con liên tiếp kết thúc tại index  i - 1
new_set: Dùng tập các dãy con liên tiếp kết thúc tại index i - 1 để OR thêm với i
Bản thân ai cũng là 1 dãy con liên tiếp kết thúc tại i sẽ dùng cho bước sau nên ta thêm vào new_set và ans
VD: index from 0:
i = 0: ans = [a0], new_set = [a0], s = [a0]
i = 1:
+/ new_set = (a0|a1), ans = (a0, //a0|a1)
+/ ans = (a0, //a0|a1, a1); new_set = (a0|a1, a1)
+/ s = (a0|a1, a1)
i = 2:
+/ new_set = (a0|a1|a2, a1|a2), ans = (a0, a0|a1, a1, //a0|a1|a2, a1|a2);
+/ ans = (a0, a0|a1, a1,// a0|a1|a2, a1|a2, a2);  new_set = (a0|a1|a2, a1|a2, a2),
+/ s = (a0|a1|a2, a1|a2, a2),
i = 3:
+/ new_set = (a0|a1|a2|a3, a1|a2|a3, a2|a3), ans = (a0, a0|a1, a1, a0|a1|a2, a1|a2, a2, a0|a1|a2|a3, a1|a2|a3, a2|a3);
+/ ans = (a0, a0|a1, a1, a0|a1|a2, a1|a2, a2, a0|a1|a2|a3, a1|a2|a3, a2|a3, a3); ...
'''