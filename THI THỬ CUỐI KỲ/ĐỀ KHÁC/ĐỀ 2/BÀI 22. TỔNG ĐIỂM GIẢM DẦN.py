class ThiSinh:
    def __init__(self, x, ten, ngaySinh, mon1, mon2, mon3):
        self.ma = x
        self.ten = ten
        self.ngaySinh = ngaySinh
        self.mon1 = mon1
        self.mon2 = mon2
        self.mon3 = mon3
        self.tong = self.mon1 + self.mon2 + self.mon3
    def __str__ (self):
        return f"{self.ma} {self.ten} {self.ngaySinh} " + "{:.1f}".format(self.tong)

if __name__ == "__main__":
    t = int(input())
    a = []
    for i in range(t): a.append(ThiSinh(i + 1, input(), input(), float(input()), float(input()), float(input())))
    a.sort(key = lambda x: -x.tong)
    for x in a: print(x)