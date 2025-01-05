class ThiSinh:
    def __init__(self, ma, ten, dtb, xl):
        self.ma = ma
        self.ten = ten
        self.dtb = dtb
        self.xl = xl

    def __str__(self):
        return "{} {} {:.2f} {}".format(self.ma, self.ten, self.dtb, self.xl)

t = int(input())
ds = []
for i in range(t):
    ma = "TS0" + "{:d}".format(i+1)
    ten = input()
    d1 = float(input())
    if d1 > 10: d1 /= 10
    d2 = float(input())
    if d2 > 10: d2 /= 10
    dtb = (d1 + d2) / 2
    xl = ""
    if dtb < 5:
        xl = "TRUOT"
    elif dtb < 8:
        xl = "CAN NHAC"
    elif dtb <= 9.5:
        xl = "DAT"
    else:
        xl = "XUAT SAC"
    ds.append(ThiSinh(ma, ten, dtb, xl))
rs = sorted(ds, key= lambda x: x.dtb, reverse=True)
for i in rs:
    print(i)