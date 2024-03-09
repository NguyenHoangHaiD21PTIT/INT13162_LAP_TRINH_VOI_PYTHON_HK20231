def res(n):
    if n % 7 ==0: return n 
    dem = 1
    check = 0 #Giả sử chưa tìm được số chia hết cho 7
    while (dem <= 1000):
        tmp = str(n)
        n+=int(tmp[::-1]) #Cộng thêm một lượng là số đảo
        if n%7 == 0:
            check = 1 
            return n #Thấy số đó rồi thì trả kết quả
        dem+=1 #Chưa thấy thì phải làm tiếp bước tiếp theo 
    if check == 0: return -1 #Quá 1000 bước không có kết quả
        
for _ in range(int(input())):
    n = int(input())
    print(res(n))