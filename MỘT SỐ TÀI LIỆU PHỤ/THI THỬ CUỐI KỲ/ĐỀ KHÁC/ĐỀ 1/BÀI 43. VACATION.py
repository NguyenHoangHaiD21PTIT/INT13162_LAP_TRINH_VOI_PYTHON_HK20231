hang, cot = map(int, input().split())
a = []
for _ in range(hang): a.append(input())
b = [["x"] * hang for _ in range (cot)]
for i in range (cot):
    for j in range (hang): b[i][j] = a[j][i]
res = 0; tmp = 0
for i in range (cot):
    ok = 1
    for j in range(hang):
        if b[i][j] == 'x':
            ok = 0
            break
    if ok == 1:tmp += 1
    else:
        res = max(res, tmp)
        tmp = 0
res = max(res, tmp)
print(res)