class ThayCo:
    def __init__(self, x, name, mxt, tin, chuyen):
        self.id = "GV" + "{:02d}".format(x)
        self.name = name
        self.mxt = mxt
        self.tin = tin
        self.chuyen = chuyen
        p = self.mxt[1]
        p1 = self.mxt[0]
        if p == '1': self.uutien = 2.0
        elif p == '2': self.uutien = 1.5
        elif p == '3': self.uutien = 1.0
        else: self.uutien = 0.0
        if p1 == 'A': self.mon = "TOAN"
        elif p1 == 'B': self.mon = "LY"
        else: self.mon = "HOA"
        self.tong = self.tin * 2.0 + self.chuyen + self.uutien
        if self.tong >= 18.0: self.status = "TRUNG TUYEN"
        else: self.status = "LOAI"
    def __str__(self):
        return "{} {} {} {:.1f} {}".format(self.id, self.name, self.mon, self.tong, self.status)
if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n): a.append(ThayCo(i + 1, input(), input(), float(input()), float(input())))
    a.sort(key=lambda x: x.tong, reverse=True)
    for x in a: print(x)








