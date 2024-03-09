class KhoHang:
    def __init__(self, id, ten, sl, dongia, chietkhau):
        self.ten = ten.strip()
        self.id = id
        self.sl = sl
        self.dongia = dongia
        self.chietkhau = chietkhau
        self.tongtien = self.sl * self.dongia - self.chietkhau  
    def __str__(self):
        return f'{self.id} {self.ten} {int(self.sl)} {int(self.dongia)} {int(self.chietkhau)} {int(self.tongtien)}'
if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n): a.append(KhoHang(input(), input(), int(input()), int(input()), int(input())))
    a.sort(key = lambda x: -x.tongtien)
    for x in a: print(x)