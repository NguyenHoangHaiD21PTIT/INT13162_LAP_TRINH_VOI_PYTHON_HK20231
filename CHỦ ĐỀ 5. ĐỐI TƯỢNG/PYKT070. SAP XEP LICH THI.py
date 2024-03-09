class Monthi:
    def __init__(self, idm, name, hinhthuc):
        self.idm = idm
        self.name = name
        self.hinhthuc = hinhthuc
class Cathi:
    def __init__(self, x, ngay, gio, phong):
        self.idct = "C{:03d}".format(x)
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
    def solve(self, mamon, nhomhp, sosv):
        self.idmon = mamon
        self.nhomhp = nhomhp
        self.sosv = sosv
    def __lt__(self, other):
        a1 = self.ngay.strip().split("/")
        a2 = other.ngay.strip().split("/")
        if a1[2] != a2[2]: return a1[2] < a2[2]
        if a1[1] != a2[1]: return a1[1] < a2[1]
        if a1[0] != a2[0]: return a1[0] < a2[0]
        if self.gio != other.gio: return self.gio < other.gio
        return self.idct < other.idct
class LichThi:
    def __init__(self, idcathi, idmon, nhomhp, sosv):
        self.idcathi = idcathi
        self.idmon = idmon
        self.nhomhp = nhomhp
        self.sosv = sosv
if __name__ == "__main__":
    f = open('MONTHI.in', 'r')
    n = int(f.readline().strip())
    mp1 = dict()
    a = []
    for i in range(n):
        a.append(Monthi(f.readline().strip(), f.readline().strip(), f.readline().strip()))
        mp1[a[i].idm] = a[i].name
    f = open('CATHI.in', 'r')
    m = int(f.readline().strip())
    mp2 = dict()
    b = []
    for i in range(m):
        b.append(Cathi(i + 1, f.readline().strip(), f.readline().strip(), f.readline().strip()))
        mp2[b[i].idct] = "{} {} {}".format(b[i].ngay, b[i].gio, b[i].phong)
    b.sort()
    f = open('LICHTHI.in', 'r')
    p = int(f.readline().strip())
    c = []
    for _ in range(p):
        idcathi, idmon, nhomhp, sosv = f.readline().strip().split()
        c.append(LichThi(idcathi, idmon, nhomhp, sosv))
    for x in b:
        for y in c:
            if x.idct == y.idcathi:
                x.solve(y.idmon, y.nhomhp, y.sosv)
                break
    for x in b:
        print("{} {} {} {} {} {}".format(x.ngay, x.gio, x.phong, mp1[x.idmon], x.nhomhp, x.sosv))
