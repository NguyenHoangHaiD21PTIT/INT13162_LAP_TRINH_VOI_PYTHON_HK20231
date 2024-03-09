s = input()
start = 0; end = 0 
while start < len(s):
    tmp = max(s[start::])
    for i in range(start, len(s)):
        if s[i] == tmp:
            print(s[i], end = "")
            end = i 
    start = end + 1