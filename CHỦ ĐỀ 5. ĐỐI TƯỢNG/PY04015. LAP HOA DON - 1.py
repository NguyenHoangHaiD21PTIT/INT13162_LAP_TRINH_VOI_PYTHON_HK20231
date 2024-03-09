from math import *
class TienNuoc:
    def __init__(self, x, name, dau, cuoi):
        self.id = "KH" + "{:02d}".format(x)
        self.name = name
        self.dau = dau
        self.cuoi = cuoi
        p = self.cuoi - self.dau
        if p <= 50:
            self.tong = round(p * 100 * 102.0 / 100)
        elif 51 <= p <= 100:
            tmp1 = 50 * 100 + (p - 50) * 150
            self.tong = round(tmp1 * 103.0 / 100)
        else:
            tmp2 = 50 * 250 + (p - 100) * 200
            self.tong = round(tmp2 * 105.0 / 100)
    def __str__(self): return f"{self.id} {self.name} {self.tong}"
if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n): a.append(TienNuoc(i + 1, input(), int(input()), int(input())))
    a.sort(key=lambda x: - x.tong)
    for x in a: print(x)