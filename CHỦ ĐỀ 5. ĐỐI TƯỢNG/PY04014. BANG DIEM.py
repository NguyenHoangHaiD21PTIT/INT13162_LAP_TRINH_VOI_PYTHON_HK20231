def custom_round(number, decimal_places):
    factor = 10 ** decimal_places
    rounded_number = int(number * factor + 0.5) / factor
    return rounded_number
class HSinh:
    def __init__(self, x, name, a):
        self.id = "HS" + "{:02d}".format(x)
        self.name = name
        self.tbc = custom_round(((a[0] + a[1]) * 2.0 + sum(a[2:])) / 12.0, 1)
        if self.tbc >= 9:
            self.xeploai = "XUAT SAC"
        elif self.tbc >= 8:
            self.xeploai = "GIOI"
        elif self.tbc >= 7:
            self.xeploai = "KHA"
        elif self.tbc >= 5:
            self.xeploai = "TB"
        else:
            self.xeploai = "YEU"

    def __str__(self):
        return f"{self.id} {self.name} {self.tbc} {self.xeploai}"

if __name__ == "__main__":
    n = int(input())
    a = []
    for x in range(n):
        s = input()
        b = list(map(float, input().split()))
        a.append(HSinh(x + 1, s, b))

    a.sort(key=lambda x: (-x.tbc, x.id))

    for x in a:
        print(x)
