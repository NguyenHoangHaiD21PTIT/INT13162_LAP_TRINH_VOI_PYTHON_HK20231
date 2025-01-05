ten, cc, kt, btl, thi = input(), float(input()), float(input()), float(input()), float(input())
tk = cc * 0.1 + kt * 0.1 + btl * 0.2 + thi * 0.6
diemChu, xepLoai = "", ""
if tk >= 8.5: diemChu = "A"; xepLoai = "Gioi"
elif tk >=7: diemChu = "B"; xepLoai = "Kha"
elif tk >=5.5: diemChu = "C"; xepLoai = "Trung binh"
elif tk >=4: diemChu = "D"; xepLoai = "Trung binh kem"
else: diemChu = "F"; xepLoai = "Kem"
print(ten)
print(diemChu); print(xepLoai)