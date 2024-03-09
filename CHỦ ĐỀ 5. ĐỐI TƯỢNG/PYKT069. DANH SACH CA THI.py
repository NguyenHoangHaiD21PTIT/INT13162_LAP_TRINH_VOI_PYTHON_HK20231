class CaThi:
    def __init__(self, x, ngaythi, giothi, phongthi):
        self.id = "C" + "{:03d}".format(x)
        self.ngaythi = ngaythi.strip()
        self.giothi = giothi.strip()
        self.phongthi = phongthi.strip()
        a = list(map(int, self.ngaythi.split("/")))
        b = list(map(int, self.giothi.split(":")))
        self.ngay = a[0]
        self.thang = a[1]
        self.nam = a[2]
        self.gio = b[0]
        self.phut = b[1]

    def __str__(self):
        return f'{self.id} {self.ngaythi} {self.giothi} {self.phongthi}'

if __name__ == "__main__":
    file = open('VANBAN.in', 'r')
    n = int(file.readline())
    a = [] 
    for i in range(n):
        tmp = CaThi(i + 1, file.readline(), file.readline(), file.readline())
        a.append(tmp)

    a.sort(key=lambda x: (x.nam, x.thang, x.ngay, x.gio, x.phut))

    for item in a:
        print(item)