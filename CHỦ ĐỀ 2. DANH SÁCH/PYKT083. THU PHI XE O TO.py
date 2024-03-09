class PhuongTien:
    def __init__(self, bienso, loai, soghe, status, ngay):
        self.bienso = bienso
        self.loai = loai
        self.soghe = soghe
        self.status = status
        self.ngay = ngay
        if self.soghe == 5: self.dongia = 10000
        elif self.soghe == 7: self.dongia = 15000
        elif self.soghe == 2: self.dongia = 20000
        elif self.soghe == 29: self.dongia = 50000
        else: self.dongia = 70000

if __name__ == "__main__":
    n = int(input())
    a = []
    d = dict()  # Lưu ngày, key là ngày còn value là tiền
    for _ in range(n):
        tmp = input().strip().split()
        tmp1 = PhuongTien(tmp[0], tmp[1], int(tmp[2]), tmp[3], tmp[4])  
        a.append(tmp1)  
    
    for x in a:
        if x.ngay in d:
            if x.status == "IN": d[x.ngay] += x.dongia
        else:
            if x.status == "IN": d[x.ngay] = x.dongia
            else: d[x.ngay] = 0

    for x, y in d.items():
        print(f'{x}: {y}')


