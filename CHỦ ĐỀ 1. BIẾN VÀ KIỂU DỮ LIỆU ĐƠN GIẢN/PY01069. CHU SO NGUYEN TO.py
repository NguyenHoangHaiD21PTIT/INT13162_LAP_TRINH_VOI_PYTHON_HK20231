from collections import deque
v = []
n = int(input())
tmp = "2357"
def check(s):
    z = set(s)
    if len(z) != 4: return False
    elif s[-1] == "2": return False
    return True
def gen():
    #Bước 1: Khởi tạo
    q = deque()
    for x in tmp: q.append(x)
    #Bước 2: Lặp
    while True:
        p = q.popleft() #Lôi đỉnh hàng đợi ra
        if len(p) == n: break
        #Từ đỉnh hàng đợi sẽ loang sang cấu hình khác. Đỉnh dài n rồi thì tất nhiên không thể loang thêm
        for x in tmp:
            tmp1 = p + x
            q.append(tmp1)
            if check(tmp1): v.append(tmp1)
gen()
for x in v: print(x)    
    