from math import sqrt
def Euclid(a, b, n):
    tong = 0 
    for i in range(n): tong += (a[i] - b[i])**2
    tong = sqrt(tong)
    return tong 

N = int(input())
n = int(input())
featureVector = list(map(float, input().split()))
res = 10**9 
person = ""
kq = []
listVec = []
if N == 3:
    print("INVALID INPUT")
else:
    for i in range(N - 3):
        tmp = input().split()
        listVec.append(tmp)

if n > 1024: print("INVALID INPUT")
else:
    for tmp in listVec:
        ten = tmp[0]  
        vector = list(map(float, tmp[1:])) 
        similarity = Euclid(featureVector, vector, n)
        kq.append(similarity)
        if similarity < res:
            res = similarity
            person = ten
    res = [round(value, 4) for value in kq]
    print(person, res)