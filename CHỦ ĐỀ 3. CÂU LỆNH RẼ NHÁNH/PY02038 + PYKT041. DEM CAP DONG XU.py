from math import *

n = int(input())
a = []
for i in range(n): a.append(input())
row = [0] * n 
col = [0] * n 
res = 0
for i in range(n):
    for j in range(n): 
        if a[i][j] == "C": 
            row[i]+=1 
            col[j]+=1 
for i in row:
    if i>=2: res+= i * (i - 1) //2 
for j in col:
    if j>=2: res+= j * (j - 1) //2 
print(res)