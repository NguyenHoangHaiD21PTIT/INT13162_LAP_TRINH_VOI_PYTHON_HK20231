d = dict()
class NhanVien:
    def __init__(self, id, ten, luongcb, day):
        self.id = id
        self.ten = ten
        self.luongcb = luongcb * 1000
        self.day = day
        loai = self.id[0]
        sonam = int(self.id[1:3:])
        self.phongban = self.id[3::]
        if 1 <=sonam <=3:
            if loai == "A" or loai == "B": self.heso = 10 
            elif loai =="C": self.heso = 9
            else: self.heso = 8
        elif 4 <=sonam <=8:
            if loai =="A": self.heso = 12
            elif loai =="B": self.heso = 11
            elif loai =="C": self.heso = 10
            else: self.heso = 9
        elif 9 <=sonam <= 15:
            if loai =="A": self.heso = 14
            elif loai =="B": self.heso = 13
            elif loai =="C": self.heso = 12
            else: self.heso = 11
        else:
            if loai =="A": self.heso = 20
            elif loai =="B": self.heso = 16
            elif loai =="C": self.heso = 14
            else: self.heso = 13
        self.tongluong = self.luongcb * self.day * self.heso
    def __str__(self):
        return f"{self.id} {self.ten} {d[self.phongban]} {self.tongluong}"

if __name__ == "__main__":
    m = int(input())
    for _ in range (m):
        a = input().split()
        res = ""
        for i in range (1, len(a)): res+=a[i]+" "
        d[a[0]] = res.strip() 
    n = int(input())
    x = []
    for _ in range (n):
        tmp = NhanVien(input(), input(), int(input()), int(input()))
        x.append(tmp)
    for p in x: print(p)