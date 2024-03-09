mp = dict()
class CaThi:
    def __init__(self, x, mamon, ngaythi, giothi, nhomthi):
        self.id = "T{:03d}".format(x)
        self.mamon = mamon
        self.tenmon = mp[mamon]
        self.ngaythi = ngaythi
        self.giothi = giothi
        self.nhomthi = nhomthi
        tmp1 = self.ngaythi.split("/")
        tmp2 = self.giothi.split(":")
        self.ngay = int(tmp1[0])
        self.thang = int(tmp1[1])
        self.nam = int(tmp1[2])
        self.gio = int(tmp2[0])
        self.phut = int(tmp2[1])
    def __str__(self):
        return f"{self.id} {self.mamon} {self.tenmon} {self.ngaythi} {self.giothi} {self.nhomthi}"
if __name__ == "__main__":
    n, m = map(int, input().split())
    for i in range(n):
        s1, s2 = input(), input()
        mp[s1] = s2 
    a = []
    for i in range(m):
        tmp = input().split()
        a.append(CaThi(i + 1, tmp[0], tmp[1], tmp[2], tmp[3]))
    a = sorted(a, key=lambda x: (x.nam, x.thang, x.ngay, x.gio, x.phut, x.mamon))
    for x in a: print(x)