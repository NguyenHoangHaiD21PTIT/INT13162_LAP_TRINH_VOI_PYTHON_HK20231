import csv
with open("iris.csv", 'r') as f:
    reader = csv.DictReader(f)
    data = []
    for row in reader: data.append(row)
for row in data: print(row)
t = int(input())
for _ in range(t):
    species, typeLen, typeStat = input().split()
    speData = []
    for row in data:
        if row['species']==species: speData.append(row)
    if not speData:
        print("Invalid")
        continue
    listLen = []
    for row in speData: listLen.append(float(row[typeLen]))
    if typeStat == "min": print(min(listLen))
    elif typeStat == "max": print(max(listLen))
    elif typeStat == "sum": print(sum(listLen))
    elif typeStat == "avg": print(round(sum(listLen) / len(listLen), 2))
    