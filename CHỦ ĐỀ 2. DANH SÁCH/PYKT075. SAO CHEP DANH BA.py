class DanhBa:
    def __init__(self, ten, sdt, ngay):
        self.ten = ten
        self.sdt = sdt
        self.ngay = ngay.strip()
        a = list(self.ten.split())
        self.tencuoi = a[-1]
        self.ho= a[0]
        self.dem =""
        for i in range(1, len(a) -1): self.dem+=a[i] + ' '
    def __str__ (self):
        return "{}: {} {}".format(self.ten, self.sdt, self.ngay[4::].strip())
file = open("SOTAY.txt", 'r')
a = []
for line in file: a.append(line.strip())
b = []
i = 0
while(i<len(a)):
    if(a[i][:4:]=="Ngay"):
        s = a[i] #Lưu thông tin ngày
        tmp = i + 1
        while(a[tmp][:4:]!="Ngay"):
            tmp1 = DanhBa(a[tmp], a[tmp + 1], s)
            b.append(tmp1)
            tmp+=2 
            if(tmp>=len(a)): break
    i = tmp
file.close()
b.sort(key = lambda x: (x.tencuoi, x.ho, x.dem))
out = open("DIENTHOAI.txt", 'w')
for i in b: out.write(i.__str__() + "\n")
out.close()