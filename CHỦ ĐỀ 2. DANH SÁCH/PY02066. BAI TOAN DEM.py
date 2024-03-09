from sys import stdin
n = int(input())
mark = [0] * 250
check = True
Max = -1
for line in stdin:
    a = list(map(int, line.split()))
    for x in a:
        Max = max(Max, x)
        mark[x] = 1 
for i in range (1, Max + 1):
    if mark[i] == 0:
        print(i)
        check = False
if check: print("Excellent!")