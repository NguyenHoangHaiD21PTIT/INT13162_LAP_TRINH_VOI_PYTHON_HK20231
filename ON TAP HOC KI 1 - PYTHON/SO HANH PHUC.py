def check(n):
    visited = set() 
    while n!=1 and n not in visited:
        visited.add(n)
        tong = 0 
        for x in str(n): tong+=int(x)**2 
        n = tong
    return n ==1 
n = int(input())
if check(n): print("YES")
else: print("NO")
