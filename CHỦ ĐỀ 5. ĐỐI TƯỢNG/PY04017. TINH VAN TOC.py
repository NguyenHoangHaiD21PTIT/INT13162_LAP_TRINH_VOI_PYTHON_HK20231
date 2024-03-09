class Cuaro:
    def __init__(self, name, donvi, vedich):
        self.name = name
        self.donvi = donvi
        self.vedich = vedich
        a = self.name.strip().split()
        b = self.donvi.strip().split()
        res = ""
        for x in b: res += x[0]
        for x in a: res += x[0]
        self.id = res
        c = self.vedich.strip().split(":")
        self.chenh = int(c[0]) + int(c[1]) / 60.0 - 6.0
        self.tocdo = round(120.0 / self.chenh)
    
    def getchenh(self):
        return self.chenh

    def __str__(self):
        return f"{self.id} {self.name} {self.donvi} {self.tocdo} Km/h"
    
if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n): a.append(Cuaro(input().strip(), input().strip(), input().strip()))
    a.sort(key=lambda x: x.getchenh())
    for x in a: print(x)