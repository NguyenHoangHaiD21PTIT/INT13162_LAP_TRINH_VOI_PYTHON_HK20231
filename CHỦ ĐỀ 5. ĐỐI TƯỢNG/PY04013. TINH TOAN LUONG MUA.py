class TramMua:
    def __init__(self, name, bd, kt, luongmua):
        self.name = name.strip()
        self.bd = bd.strip()
        self.kt = kt.strip()
        self.luongmua = luongmua
        a = self.bd.split(":")
        b = self.kt.split(":")
        x1, x2, x3, x4 = int(a[0]), int(a[1]), int(b[0]), int(b[1])
        self.giomua = (x3 * 60 + x4 - x1 * 60 - x2) / 60.0  # Tính tổng giờ mưa
if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        name = input()
        bd = input()
        kt = input()
        luongmua = float(input())
        a.append(TramMua(name, bd, kt, luongmua))
    v = []  # Lưu tên trạm mưa
    mp1 = dict()  # mp1[i] lưu tổng lượng mưa tại trạm thứ i
    mp2 = dict()  # mp2[i] lưu tổng số giờ mưa tại trạm thứ i
    for x in a:
        s = x.name  # Tên trạm mưa
        time = x.giomua  # Lấy tổng thời gian mưa lần đó tại trạm đó
        mua = x.luongmua  # Lấy tổng lượng mưa lần đó trạm đó
        if s in mp1:
            mp1[s] += mua  # Cộng thêm lượng mưa lần đang xét
            mp2[s] += time  # Cộng thêm tổng số giờ mưa đang xét
        else:
            mp1[s] = mua
            mp2[s] = time
            v.append(s)
    for i in range(len(v)):
        print("T" + str(i + 1).zfill(2) +" " + v[i], end = " ")
        tmp = mp1[v[i]] / mp2[v[i]]
        print("%.2f" %tmp)

