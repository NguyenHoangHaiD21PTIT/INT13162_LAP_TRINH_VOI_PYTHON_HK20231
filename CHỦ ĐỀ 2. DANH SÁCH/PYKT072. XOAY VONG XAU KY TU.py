def rotate(a, b):
    #Giữ nguyên 1 xâu rồi dùng xâu còn lại biến đổi tính số bước
    #trong đó a là xâu chuẩn, b là cái phải theo a
    if len(a)!=len(b): return -1;
    s = a 
    for i in range (0, len(a) + 1):
        if s == b: return i
        s = s[1::] + s[0] #Nhét chữ cái đầu xuống cuối
    return -1
def soBuoc(a):
    ans = 1000000
    for x in a:
        #Lấy 1 xâu x làm chuẩn, bắt các xâu khác y xoay theo xâu chuẩn đó
        cnt = 0 
        for y in a:
            tmp = rotate(y, x)
            if(tmp==-1): return -1 
            cnt+=tmp 
        ans = min(ans, cnt)
    return ans 
a =[]
for i in range(int(input())): a.append(input())
print(soBuoc(a))
