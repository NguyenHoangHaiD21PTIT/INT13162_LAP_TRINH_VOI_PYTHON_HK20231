class CongNhan:
    def __init__ (self, ma, ten, vao, ra):
        self.ten = ten
        self.ma = ma
        self.ra = ra 
        self.vao = vao
        a, b = map(int, self.ra.split(":"))
        c, d = map(int, self.vao.split(":"))
        self.tongTG = (a*60 + b) - (c*60 + d) - 60
        self.gio = self.tongTG//60
        self.phut = self.tongTG%60
        if self.tongTG>=480: self.status = "DU"
        else: self.status = "THIEU"
    def __str__ (self):
        return f"{self.ma} {self.ten} {self.gio} gio {self.phut} phut {self.status}"

n = int(input())
a = []
for _ in range(n): a.append(CongNhan(input(), input(), input(), input()))
a.sort(key = lambda x: -x.tongTG)
for x in a: print(x)
