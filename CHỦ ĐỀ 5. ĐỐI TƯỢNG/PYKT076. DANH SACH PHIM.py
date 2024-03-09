d = dict()
class Phim:
    def __init__(self, x, TheLoai, NgayChieu, TenPhim, SoTap):
        self.MaPhim = "P" + "{:03d}".format(x)
        self.TheLoai = d[TheLoai]
        self.NgayChieu = NgayChieu 
        self.TenPhim = TenPhim
        self.SoTap = SoTap
        a = list(map(int, self.NgayChieu.split("/")))
        self.ngay = int(a[0])
        self.thang = int(a[1])
        self.nam = int(a[2])
    def __str__ (self):
        return "{} {} {} {} {}".format(self.MaPhim, self.TheLoai, self.NgayChieu, self.TenPhim, self.SoTap)
        
n, m = map(int, input().split())
for i in range(n):
    s = "TL" + "{:03d}".format(i + 1)
    s1 = input().strip()
    d[s] = s1 
a = []
for i in range(0, m):
    tmp = Phim(i + 1, input(), input(), input(), (int(input().strip())))
    a.append(tmp) 
a.sort(key = lambda x: (x.nam, x.thang, x.ngay, x.TenPhim, -x.SoTap))
for x in a: print(x)


