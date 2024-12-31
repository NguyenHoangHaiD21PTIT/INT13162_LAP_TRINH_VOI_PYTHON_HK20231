import json
with open("flights.json", 'r') as f: data = json.load(f)
listFlight = data['flights']# Lấy ra danh sách các chuyến bay
t = int(input())
for _ in range(t):
    nam, loai = input().split()  
    yearData = []
    for x in listFlight:
        if x['year']==nam: yearData.append(x)
    if len(yearData) == 0: print("Invalid")
    else:
        soKhach = []
        for x in yearData: soKhach.append(int(x['passengers']))
        if loai == "min": print(min(soKhach))
        elif loai == "max": print(max(soKhach))
        elif loai == "sum": print(sum(soKhach))
        elif loai == "avg": print(round(sum(soKhach) / len(soKhach), 5))

