def chuanhoa(s):
    a = s.strip().split()
    res = ""
    for x in a: res += x.capitalize() + " "
    return res

from math import *
class SinhVien:
    def __init__(self, x, name, x1, x2, x3):
        self.id = "SV" + "{:02d}".format(x)
        self.name = chuanhoa(name)
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.tbc = ceil((self.x1 * 3 + self.x2 * 3 + self.x3 * 2) / 8.0 * 100) / 100
    
    def __str__(self):
        return f"{self.id} {self.name}{self.tbc:.2f}"

if __name__ == "__main__":
    n = int(input())
    b = [] #vector lưu mảng điểm
    a = [] #Vector lưu sinh viên
    for i in range(n):
        a.append(SinhVien(i + 1, input().strip(), float(input().strip()), float(input().strip()), float(input().strip())))
    mp = dict()  # Đếm tần suất các giá trị khác nhau của điểm
    for x in a:
        tmp = x.tbc
        if tmp in mp: mp[tmp] += 1
        else:
            b.append(tmp)
            mp[tmp] = 1

    # Sắp xếp mảng các điểm khác nhau giảm dần
    b.sort(reverse=True)

    mp1 = dict()  # Vector lưu hạng điểm
    mp1[b[0]] = 1 #Các bạn điểm cao nhất sẽ là hạng 1 
    x = 1
    for i in range(1, len(b)):
        x += mp[b[i - 1]]
        mp1[b[i]] = x
    a.sort(key=lambda x: (-x.tbc, x.id))

    for p in a: print(str(p) + " " +str(mp1[p.tbc]))
