class Team:
    def __init__(self, x, tenTeam, tenTruong):
        self.id = 'Team{:02d}'.format(x)
        self.tenTeam = tenTeam
        self.tenTruong = tenTruong
class ThiSinh:
    def __init__(self, x, hoTen, maTeam):
        self.maTS = "C{:03d}".format(x)
        self.hoTen = hoTen
        self.maTeam = maTeam
    def __str__(self):
        return '{} {}'.format(self.maTS, self.hoTen)

if __name__== '__main__':
    d = dict()
    n = int(input())
    a = []
    for i in range(n):
        tmp = Team(i + 1, input(), input())
        a.append(tmp)
        d[tmp.id] = tmp.tenTeam + " " + tmp.tenTruong
    m = int(input())
    b = []
    for i in range(m):
        tmp = ThiSinh(i + 1, input(), input())
        b.append(tmp)
    b.sort(key = lambda x: x.hoTen)
    for x in b: 
        print(x, d[x.maTeam])