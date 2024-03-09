n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for j in range(n):
    column = [matrix[i][j] for i in range(n)]
    column.sort()
    for i in range(n):
        matrix[i][j] = column[i]

for i in range(n):
    print(" ".join(map(str, matrix[i])))