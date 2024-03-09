from collections import deque
v = []
n = int(input())
tmp = "ABC"
def check(s):
    cnta = 0
    cntb = 0 
    cntc = 0
    for x in s:
        if x == 'A': cnta+=1 
        elif x=='B': cntb+=1 
        else: cntc+=1 
    if cnta and cntb and cntc and cnta <= cntb and cntb <= cntc: return True
    else: return False
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
    