n = int(input())
a = list(map(int, input().split()))
preSum = [0] * n
preSum[0] = a[0]
for i in range(1, n): preSum[i] = preSum[i - 1] + a[i]
tong, tich = 0, 1 
for x in preSum: 
    tong+=x; tich*=x;  
print(tong, tich)
