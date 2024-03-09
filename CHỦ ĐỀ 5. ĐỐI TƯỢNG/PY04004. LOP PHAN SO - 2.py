import math
def BCNN(a, b):
    return a* b//math.gcd(a, b)

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu;
        self.mau = mau;

    def rutgon(self):
        k = math.gcd(self.tu, self.mau);
        self.tu = self.tu // k;
        self.mau = self.mau // k;

    def __str__(self):
        return f"{self.tu}/{self.mau}";

    def congps(self, p):
        self.rutgon();
        p.rutgon();
        x = BCNN(self.mau, p.mau);
        kq1 = x // self.mau * self.tu + x // p.mau * p.tu;
        kq = PhanSo(kq1, x);
        kq.rutgon();
        return kq;

if __name__ ==  '__main__':
    a, b, c, d = [int(x) for x in input().split()];
    g = PhanSo(a, b);
    h = PhanSo(c, d);
    t = g.congps(h);
    t.rutgon();
    print(t);