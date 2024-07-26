n = int(input())
a = []
for _ in range(n): a.append(int(input()))

#index nho nhat ma tai do >=x, tim tu L den cuoi mang
def low(arr, L, x):
    R = len(arr) - 1
    while L < R:
        mid = (L + R) //2  
        if arr[mid] < x: L = mid + 1
        else: R = mid
    return L

z = sorted(set(a))
m = [[] for i in z]
first = [0] * len(z)
for i in range(n):
    a[i] = low(z, 0, a[i])
    m[a[i]].append(i)
'''
Dau tien, ta se gan cho moi a[i] phan biet mot tri so
VD = [2, 4, 1, 2, 2, 5, 1] --> [1, 2, 4, 5]
--> Dict///1: 0, 2: 1, 4: 2, 5: 3
m[a[i]]: Luu tat ca nhung index i trong mang a ma a[i] goc = a[value] goc
'''

#Phan tu ben trai dau tien lon hon
st1 = []; l = [-1] * n
for i in range (n):
    while st1 and a[st1[-1]] <= a[i]: st1.pop()
    if st1: l[i] = st1[-1]
    else: l[i] = -1 
    st1.append(i)

#Phan tu ben phai dau tien lon hon
st2 = []; r = [-1] * n
for i in range (n - 1, -1, -1):
    while st2 and a[st2[-1]] <= a[i]: st2.pop()
    if st2: r[i] = st2[-1]
    else: r[i] = n 
    st2.append(i)

#Tim so phan tu 
def count(arr, start, x):
    if start >= len(arr) or x < arr[start]: return 0
    pos = low(arr, start, x)
    if arr[pos] > x: pos-=1
    return pos - start + 1

s = 0
for i in range(n):
    if l[i] != -1: s += 1
    if r[i] != n: s += 1
    x = count(m[a[i]], first[a[i]], r[i] - 1)
    s += (x - 1) * x // 2
    first[a[i]] += x
print(s)