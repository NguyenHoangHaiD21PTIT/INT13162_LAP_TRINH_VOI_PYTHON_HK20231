s = input()
k = 1
for i in range(1, len(s)) :
    if s[i] != s[i - 1] :
        print(s[i - 1], end = "")
        print(k,end = "")
        k = 1
    else : k += 1
print(s[-1], k, sep ="")