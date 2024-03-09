def chuanhoa(s):
    a = s.strip().split()
    res = ""
    for x in a:
        res += x.capitalize() + " "
    return res
class User:
    def __init__(self, x, name, loai, dau, cuoi):
        self.id = "KH" + "{:02d}".format(x)
        self.name = chuanhoa(name)
        self.loai = loai
        self.dau = dau
        self.cuoi = cuoi
        sodien = self.cuoi - self.dau
        if self.loai == "A":
            self.dinhmuc = 100
        elif self.loai == "B":
            self.dinhmuc = 500
        else:
            self.dinhmuc = 200
        if sodien <= self.dinhmuc:
            self.indm = sodien * 450
            self.vuotdm = 0
            self.VAT = 0
        else:
            self.indm = self.dinhmuc * 450
            self.vuotdm = (sodien - self.dinhmuc) * 1000
            self.VAT = self.vuotdm //20
        self.tong = self.indm + self.vuotdm + self.VAT
    def gettong(self):
        return self.tong
    def __str__(self):
        return '{} {}{} {} {} {}'.format(self.id, self.name, self.indm, self.vuotdm, self.VAT, self.tong)

if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range (0, n):
        x = input().strip()
        tmp = input().strip().split()
        y, z, t = tmp[0], int(tmp[1]), int(tmp[2])
        p = User(i + 1, x, y, z, t)
        a.append(p)
    a.sort(key = lambda x: -x.gettong())
    for x in a: print(x)