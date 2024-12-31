class ThiSinh:
    def __init__ (self, ten, ngaySinh, mon1, mon2, mon3):
        self.ten = ten
        self.ngaySinh = ngaySinh 
        self.mon1 = mon1 
        self.mon2 = mon2
        self.mon3 = mon3 
        a = [mon1, mon2, mon3]
        a.sort()
        self.trungBinh = (a[0] * 2 + a[1] + a[2])/4
        
    def __str__ (self):
        return f"{self.ten} {self.ngaySinh} {self.trungBinh:.1f}"

n = int(input())  
a = []
for _ in range(n):
    ten = input().strip()
    ngaySinh = input().strip()
    mon1 = float(input().strip())
    mon2 = float(input().strip())
    mon3 = float(input().strip())
    a.append(ThiSinh(ten, ngaySinh, mon1, mon2, mon3))
a.sort(key=lambda x: -x.trungBinh)
for ts in a: print(ts)

