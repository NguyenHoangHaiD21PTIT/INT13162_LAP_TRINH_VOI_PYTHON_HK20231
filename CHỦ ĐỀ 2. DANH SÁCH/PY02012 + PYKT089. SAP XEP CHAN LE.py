from sys import stdin
n = int(input())
a = []
d = [0] * n #d[i] = 0 tức là vị trí i là số chẵn và ngược lại 
chan = []
le = []

for line in stdin:
    x = list(map(int, line.split()))
    for i in x: a.append(i)
    
#Phân loại số chẵn, lẻ và đánh dấu đâu là vị trí có số chẵn
for i in range (n):
    if a[i]%2==1: 
        le.append(a[i])
        d[i] = 1 
    else: 
        chan.append(a[i])
        d[i] = 0 
        
#Sắp xếp chẵn giảm lẻ tăng
chan.sort(reverse = True)
le.sort()

#In theo đề
for i in range (n):
    if d[i] == 0: #Với vị trí chứa số chẵn, lần lượt in số bé nhất, tức đỉnh list, in xong xóa
        print (str(chan[-1]), end = " ")
        chan.pop()
    else: 
        print(str(le[-1]), end = " ")
        le.pop()