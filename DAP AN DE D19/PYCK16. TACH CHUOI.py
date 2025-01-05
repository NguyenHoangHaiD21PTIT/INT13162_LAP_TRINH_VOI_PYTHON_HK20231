a = list(input().split())
minWord = []; maxWord = []; lenMax = -1; lenMin = 10**9 
for x in a: 
    if len(x)>lenMax: lenMax = len(x)
    if len(x)<lenMin: lenMin = len(x) 
for x in a:
    if len(x)==lenMax: maxWord.append(x) 
    if len(x)==lenMin: minWord.append(x)
minWord.sort(); maxWord.sort() 
for x in maxWord: print(x, len(x))
for x in minWord: print(x, len(x))