class Rectangle:
    def __init__(self, dai, rong, mau):
        self.dai = dai
        self.rong = rong
        self.mau = mau.capitalize()
        self.chuvi = (self.dai + self.rong) * 2 
        self.dientich =  self.dai * self.rong
    def __str__(self):
        if(self.dai > 0 and self.rong > 0): return '{} {} {}'.format(self.chuvi, self.dientich, self.mau)
        else: return ('INVALID')

a = input().split()
rec = Rectangle(int(a[0]), int(a[1]), (a[2]))
print(rec)
