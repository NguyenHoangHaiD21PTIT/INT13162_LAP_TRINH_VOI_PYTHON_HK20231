from math import sqrt

def doDai(a):
    tong = 0
    for i in range(len(a)): tong += a[i] * a[i]
    return sqrt(tong)

def co_sin(a, b, n):
    tichVH = 0
    for i in range(n): tichVH += a[i] * b[i]
    kq = tichVH / (doDai(a) * doDai(b))
    return kq

N = int(input())
n = int(input())
featureVector = list(map(float, input().split()))
res = -1  
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
        similarity = co_sin(featureVector, vector, n)
        kq.append(similarity)
        if similarity > res:
            res = similarity
            person = ten
    res = [round(value, 4) for value in kq]
    print(person, res)


