MN = 1000000 
POW10 = [10, 100, 1000, 10000, 100000, 1000000] # 10^i, i = 1..6
b = [1] * MN
a = [] # List các SNT cắt được

# Các số nguyên tố < 1 triệu
def ByteSieve():
    b[0] = b[1] = 0
    # xóa các số chẵn 4..n
    for i in range(4, MN, 2): b[i] = 0
    for i in range(3, int(MN ** 0.5) + 1, 2):
        if b[i]: # i prime
            # xóa các bội (i*i, n, i)
            for j in range(i * i, MN, i): b[j] = 0
    return b

def Cut(x):
    for p in POW10:
        thuong, du = divmod(x, p)
        if thuong == 0: break
        if not b[thuong]: return False
        if not b[du]: return False        
    return True


def Truncat():
    for i in range(23, MN, 2):
        if b[i]:
            if Cut(i): a.append(i)

ByteSieve()
Truncat()

from sys import stdin
for line in stdin:
    x, y = map(int, line.strip().split())
    for z in a: 
        if z>=x and z<=y: print(z, end = ' ')
    print()
