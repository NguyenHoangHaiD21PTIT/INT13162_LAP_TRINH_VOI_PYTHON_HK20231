def chuanhoa(s):
    a = s.split()
    res = ""
    for x in a: res+=x.capitalize() +" "
    return res.strip()
class TS:
    def __init__(self, x, name, diem, dantoc, kv):
        self.id = "TS" + "{:02d}".format(x)
        self.name = chuanhoa(name).strip()
        self.diem = diem
        self.dantoc = dantoc.strip()
        self.kv = kv.strip()
        self.uutien = 0.0
        if self.kv == "1": self.uutien += 1.5
        elif self.kv == "2": self.uutien += 1.0
        if self.dantoc != "Kinh": self.uutien += 1.5
        self.diemfinal = self.diem + self.uutien
        if self.diemfinal >= 20.5: self.status = "Do"
        else: self.status = "Truot"
    def __str__(self):
        return "{} {} {:.1f} {}".format(self.id, self.name, self.diemfinal, self.status)
if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range (n):
        a.append(TS(i + 1, input(), float(input()), input(), input()))
    a.sort(key = lambda x: (-x.diemfinal, x.id))
    for x in a: print(x)

