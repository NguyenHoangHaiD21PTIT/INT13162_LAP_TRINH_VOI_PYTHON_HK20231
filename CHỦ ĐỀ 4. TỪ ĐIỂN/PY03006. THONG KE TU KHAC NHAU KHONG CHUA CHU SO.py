t = int(input())
d = dict() #Tạo dict rỗng
def check(s):
    for x in s:
        if x.isdigit(): return False
    return True
for i in range(t) : 
    s = input()
    s = s.lower()
    delim = ',.?!:;()-/'
    for x in delim: s = s.replace(x, ' ')
    a = list(s.split())
    for x in a:
        if x in d: d[x]+=1 
        else: d[x] = 1 
res = list(d.items())  # Lấy danh sách cặp (key, value) từ từ điển
res.sort(key = lambda x:(-x[1], x[0]))
for x in res: 
    if check(x[0]): print(x[0], x[1], sep =" ")