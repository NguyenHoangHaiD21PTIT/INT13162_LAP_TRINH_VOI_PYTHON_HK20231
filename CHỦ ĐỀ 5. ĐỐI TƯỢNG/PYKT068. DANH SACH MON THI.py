class CaThi:
    def __init__(self, id, ten, hinhthuc):
        self.id = id.strip()
        self.ten = ten.strip()
        self.hinhthuc = hinhthuc.strip()
    def __str__(self):
        return f'{self.id} {self.ten} {self.hinhthuc}'

if __name__ == "__main__":
    n = int(input())
    a = []
    for _ in range (n):
        tmp = CaThi(input(), input(), input())
        a.append(tmp)
    a.sort(key = lambda x: x.id)
    for x in a: print(x)