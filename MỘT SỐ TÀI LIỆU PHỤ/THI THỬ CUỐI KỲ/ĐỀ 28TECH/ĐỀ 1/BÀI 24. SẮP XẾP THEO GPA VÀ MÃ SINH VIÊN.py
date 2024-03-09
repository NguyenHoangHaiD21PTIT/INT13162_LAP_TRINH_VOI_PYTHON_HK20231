def chuanHoaTen(s):
    res = ""
    a = s.split()
    for x in a: res+=x.capitalize() + " "
    return res.strip()
def chuanHoaNgaySinh(s):
    #TH1:2/12/2003
    if s[1]=="/": s = "0" + s
    #TH2:12/2/2003
    if s[4]=="/": s = s[0:3:] + "0" + s[3::]
    return s
class SinhVien:
    def __init__(self, x, name, lop, ngaySinh, gpa):
        self.id = "SV" + "{:03d}".format(x)
        self.name = chuanHoaTen(name)
        self.lop = lop
        self.ngaySinh = chuanHoaNgaySinh(ngaySinh)
        self.gpa = gpa
    def __str__(self):
        return f"{self.id} {self.name} {self.lop} {self.ngaySinh} " + "{:.2f}".format(self.gpa)
if __name__ == "__main__":
    n = int(input())
    a = []
    for x in range(n): a.append(SinhVien(x+1, input(), input(), input(), float(input())))
    a.sort(key=lambda x: -x.gpa)
    for x in a: print(x)