from sys import stdin
diff = dict()
numT = dict()
score = dict()
res = []
class DoiBong:
    def __init__ (self, ma, ten, soTran, hieuSo, diem):
        self.ma = ma
        self.ten = ten 
        self.soTran = soTran
        self.hieuSo = hieuSo
        self.diem = diem
a1 = []
for line in stdin: a1.append(line.strip())
res = 0
for i in range(len(a1) - 1):
    if a1[i] == "------------------" and a1[i + 1][0]!="#":
        res = i;
        break;
ans = []
for i in range(0, res - 3, 5):
    ma = a1[i + 1].strip()
    ten = a1[i + 2].strip()
    sotran, hieuso, diem = map(int, a1[i + 3].split())
    diff[ten] = hieuso; numT[ten] = sotran; score[ten] = diem
    ans.append(DoiBong(ma, ten, sotran, hieuso, diem))
for i in range(res + 1, len(a1)):
    s = a1[i].split("-")
    a = s[0].split()
    b = s[1].split()
    doia = ""; soBana = 0; doib = ""; soBanb = 0;
    for i in range(0, len(a) - 1): doia+=a[i] + " "
    doia = doia.strip()
    soBana = int(a[-1].strip())
    for i in range(1, len(b)): doib+=b[i] + " "
    doib = doib.strip()
    soBanb = int(b[0].strip())
    chenhlech = abs(soBanb - soBana)
    numT[doia]+=1 
    numT[doib]+=1
    if soBana > soBanb: 
        diff[doia]+=chenhlech
        diff[doib]-=chenhlech
        score[doia]+=3 
    elif soBana == soBanb:
        score[doia]+=1 
        score[doib]+=1 
    else:
        diff[doia]-=chenhlech
        diff[doib]+=chenhlech
        score[doib]+=3 

for x in ans:
    x.soTran = numT[x.ten]   
    x.hieuSo = diff[x.ten]    
    x.diem = score[x.ten] 

ans.sort(key = lambda x: (- x.diem, -x.hieuSo, x.ten))
cnt = 1
for x in ans: 
    print("#" + str(cnt), end = " ")
    print(x.ma, x.ten, x.soTran, x.hieuSo, x.diem)
    print("------------------")
    cnt+=1