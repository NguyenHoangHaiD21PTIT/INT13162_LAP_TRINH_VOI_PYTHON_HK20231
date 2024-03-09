def chenh(s1, s2):
    a = s1.split(":"); b = s2.split(":")
    x = int(b[0]) * 60 + int(b[1]) - int(a[0]) * 60 - int(a[1])
    return x
class Game:
    def __init__(self, id, name, vao, ra):
        self.id = id
        self.name = name
        self.vao = vao
        self.ra = ra
        self.tongtg = chenh(self.vao, self.ra)
        x = self.tongtg // 60
        y = self.tongtg % 60
        self.tg = str(x) + " gio " + str(y) + " phut "
    def __str__(self): return f"{self.id} {self.name} {self.tg}"
if __name__ == "__main__":
    n = int(input())
    a = []
    for _ in range(n): a.append(Game(input(), input(), input(), input()))
    a.sort(key=lambda x: -x.tongtg)
    for x in a: print(x)