class DoiBong:
    def __init__ (self, ten, tong, hieu, soBan):
        self.ten = ten
        self.tong = tong
        self.hieu = hieu
        self.soBan = soBan
    def __str__ (self):
        return f"{self.ten} {self.tong} {self.hieu} {self.soBan}"

n = int(input())
a = []
for _ in range(n):
    x = input()
    y = list(map(int, input().split()))
    a.append(DoiBong(x, y[0], y[1], y[2]))
a.sort(key = lambda x: (-x.tong, -x.hieu, -x.soBan))
for x in a: print(x)
