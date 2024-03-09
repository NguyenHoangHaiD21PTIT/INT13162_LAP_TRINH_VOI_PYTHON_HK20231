a = [1]
s = set()
s.add(1)
def gen():
    while True:
        ok = 0 #Còn số mới được thêm vào
        for x in a:
            if x < 10**18:
                if not(x*2) in s: 
                    ok = 1; 
                    a.append(x*2); s.add(x*2);
                if not(x*3) in s: 
                    ok = 1
                    a.append(x*3); s.add(x*3);
                if not(x*5) in s: 
                    ok = 1
                    a.append(x*5); s.add(x*5);
        if ok ==0: break   
    a.sort()
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2  
        if arr[mid] == target: return mid  
        elif arr[mid] < target: l = mid + 1  
        else: r = mid - 1  
    return -1  

if __name__ == "__main__":
    gen()
    for _ in range (int(input())):
        n = int(input())
        if(binary_search(a, n)!=-1 and n <= 10 ** 18):  print(binary_search(a, n) + 1)
        else: print("Not in sequence")