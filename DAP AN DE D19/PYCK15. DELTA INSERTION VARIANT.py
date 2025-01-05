N = int(input())
a = []
for i in range(N): a.append(int(input()))
kq = []
if N > 10 or N < 0: print("INVALID INPUT")
else:
    for x in a: 
        if x > 365: kq.append("INVALID INPUT")
        else: 
            k = x//11
            kq.append(2**k - 1)
    for x in kq: print(x)