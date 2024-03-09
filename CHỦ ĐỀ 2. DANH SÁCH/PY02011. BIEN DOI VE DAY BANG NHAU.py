n = int(input())
a = list(map(int, input().split()))
ans, p = 10**9, 0 #Ans là số bước, p là gf trị lựa chọn
for i in a:
    #Xét mỗi số a[i], coi rằng đó là giá trị bằng nhau mà ta sẽ ép mọi phần tử vể
    cnt = 0 #Số bước để biến những phần tử còn lại thành giá trị ta lựa chọn
    for j in a: cnt+=abs(i - j)
    if(cnt < ans): #Số bước biến đổi được giảm đi
        ans = cnt 
        p = i 
print(ans, p)