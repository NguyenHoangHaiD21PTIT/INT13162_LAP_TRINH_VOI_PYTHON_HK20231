n = int(input())
a = list(map(int, input().split()))
b = [0] * 30002
for x in a: b[x] = 1 
for i in range (1, 30001):
    if b[i] == 0:
        print(i)
        break

