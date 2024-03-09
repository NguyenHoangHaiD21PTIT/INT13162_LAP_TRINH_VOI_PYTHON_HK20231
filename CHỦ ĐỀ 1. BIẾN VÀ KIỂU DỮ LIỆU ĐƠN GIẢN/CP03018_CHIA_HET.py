n, m = map(int, input().split()) #n là số phần tử, m là số truy vấn
mul_a = 1;
a = list(map(int, input().split()))
for x in a: mul_a*=x
res = []
for i in range (1, m + 1):
    b = list(map(int, input().split()))
    mul_b = 1
    for x in b: mul_b*=x
    if mul_a%mul_b==0: res.append(i)
print(len(res))
for x in res: print(x, end = " ")
