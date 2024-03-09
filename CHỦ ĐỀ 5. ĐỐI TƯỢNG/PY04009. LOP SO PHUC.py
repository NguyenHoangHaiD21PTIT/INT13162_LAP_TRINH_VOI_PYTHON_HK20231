class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    
    def tong(self, a):
        x = self.thuc + a.thuc
        y = self.ao + a.ao
        res = SoPhuc(x, y)
        return res
    
    def nhan(self, a):
        x = self.thuc * a.thuc - self.ao * a.ao
        y = self.thuc * a.ao + self.ao * a.thuc
        res = SoPhuc(x, y)
        return res
    
    def __str__(self):
        res = ""
        res += str(self.thuc) + " "
        if self.ao < 0:
            res += "- " + str(abs(self.ao)) + "i"
        else:
            res += "+ " + str(abs(self.ao)) + "i"
        return res

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        tmp = list(map(int, input().split()))
        while len(tmp) < 4:
            tmp2 = list(map(int, input().split()))
            for x in tmp2: tmp.append(x)
        a = SoPhuc(tmp[0], tmp[1])
        b = SoPhuc(tmp[2], tmp[3])
        c = (a.tong(b)).nhan(a)
        d = (a.tong(b)).nhan(a.tong(b))
        print(c, end = ", ")
        print(d)
        t -= 1