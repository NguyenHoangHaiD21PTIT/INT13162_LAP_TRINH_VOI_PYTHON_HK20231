class ThiSinh:
    def __init__(self, name, birth, x1, x2, x3):
        self.name = name
        self.birth = birth
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
    def __str__(self):
        return "{} {} {:.1f}".format(self.name, self.birth, self.x1 + self.x2 + self.x3)

if __name__ == "__main__":
    x = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
    print(x)