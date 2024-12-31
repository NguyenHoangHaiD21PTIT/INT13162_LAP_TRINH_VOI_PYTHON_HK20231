def valid(s):
    if len(s) < 6 or len(s) > 12: return False
    checkHoa, checkThuong, checkSo, checkDB = 0, 0, 0, 0
    for x in s:
        if 'a'<=x<='z': checkThuong = 1 
        if 'A'<=x<='Z': checkHoa = 1 
        if '0'<=x<='9': checkSo = 1 
        tmp = "[$#@!]"
        for y in tmp:
            if y==x: 
                checkDB = 1 
                break 
    return checkHoa==1 and checkThuong==1 and checkSo==1 and checkDB==1 

a = input().strip().split(",")
res = []
for x in a:
    if valid(x): res.append(x)
if len(res) == 0: print("INVALID PASSWORD")
else: print(",".join(res))
