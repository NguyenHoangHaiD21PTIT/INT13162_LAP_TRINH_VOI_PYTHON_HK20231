import json
with open("tips.json", 'r') as f: data = json.load(f)
listBill = data['tips']
t = int(input())
for _ in range(t):
    ngay, soNguoi = input().split() 
    staData = []
    for x in listBill:
        if x['day']==ngay and x['size']==soNguoi: staData.append(x)
    if len(staData)==0: print("Invalid")
    else: 
        tong = 0 
        for x in staData: tong+=float(x['total_bill'])
        tbc = tong/len(staData)
        print(f"{tbc:.4f}")
