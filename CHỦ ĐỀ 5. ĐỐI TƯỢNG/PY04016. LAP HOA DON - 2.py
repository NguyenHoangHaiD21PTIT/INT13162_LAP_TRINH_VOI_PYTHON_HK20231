from datetime import datetime
def chenhlech(s1, s2):
    d = "%d/%m/%Y"
    d1 = datetime.strptime(s1, d)
    d2 = datetime.strptime(s2, d)
    return (d2 - d1).days + 1
    
class KhachHang:
    def __init__(self, x, tenkh, phong, nhan, tra, phatsinh):
        self.id = "KH" + "{:02d}".format(x)
        self.tenkh = tenkh
        self.phong = phong
        self.nhan = nhan
        self.tra = tra
        self.phatsinh = phatsinh
        self.tongngay = chenhlech(self.nhan, self.tra) + 1
        p = self.phong[0]
        if p == "1":
            self.dongia = 25
        elif p == "2":
            self.dongia = 34
        elif p == "3":
            self.dongia = 50
        else:
            self.dongia = 80
        self.tongtien = self.tongngay * self.dongia + self.phatsinh

    def __str__(self):
        return f"{self.id} {self.tenkh} {self.phong} {self.tongngay} {self.tongtien}"

    def gettong(self):
        return self.tongtien
        
if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        a.append(KhachHang(i + 1, input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip())))
    a.sort(key=lambda x: -x.gettong())
    for x in a:
        print(x)  