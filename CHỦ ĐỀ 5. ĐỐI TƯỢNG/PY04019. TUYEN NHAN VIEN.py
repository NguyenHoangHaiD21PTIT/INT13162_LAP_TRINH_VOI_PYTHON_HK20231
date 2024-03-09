from math import *
def change(a):
    if a <= 10: return a
    return a / 10.0
class TSinh:
    def __init__(self, x, name, lt, th):
        self.id = "TS0" + str(x)
        self.name = name
        self.lt = change(lt)
        self.th = change(th)
        self.tbc = (self.lt + self.th) / 2.0
        if self.tbc > 9.5: self.loai = "XUAT SAC"
        elif self.tbc >= 8.0: self.loai = "DAT"
        elif self.tbc >= 5.0: self.loai = "CAN NHAC"
        else: self.loai = "TRUOT"
    def __str__(self):
        return "{} {} {:.2f} {}".format(self.id, self.name, ceil(self.tbc * 100)/100 , self.loai)
if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        name = input()
        lt, th = float(input()), float(input())
        a.append(TSinh(i + 1, name, lt, th))
    a.sort(key = lambda x: -x.tbc)
    for x in a: print(x)