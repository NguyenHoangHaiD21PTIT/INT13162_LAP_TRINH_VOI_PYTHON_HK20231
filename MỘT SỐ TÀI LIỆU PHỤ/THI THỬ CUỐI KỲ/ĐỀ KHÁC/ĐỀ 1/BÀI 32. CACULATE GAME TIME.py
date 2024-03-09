class Gamer:
    def __init__(self, username, password, name, timeIn, timeOut):
        self.username = username
        self.password = password
        self.name = name
        self.timeIn = timeIn
        self.timeOut = timeOut
        giora = int(self.timeOut[0:2:]); phutra = int(self.timeOut[3::])
        giovao = int(self.timeIn[0:2:]); phutvao = int(self.timeIn[3::])
        self.tmp = (giora * 60 + phutra) - (giovao * 60 + phutvao)
        self.giochoi = self.tmp // 60
        self.phutchoi = self.tmp % 60
    def __str__(self):
        return f"{self.username} {self.password} {self.name} {self.giochoi} gio {self.phutchoi} phut"

if __name__=="__main__":
    t = int(input())
    a = []
    for _ in range(t): a.append(Gamer(input(), input(), input(), input(), input()))
    a.sort(key = lambda x: (-x.tmp, x.username))
    for x in a: print(x)