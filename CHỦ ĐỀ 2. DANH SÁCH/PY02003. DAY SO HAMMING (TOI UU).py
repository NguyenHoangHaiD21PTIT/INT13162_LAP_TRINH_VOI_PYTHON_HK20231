import heapq

hammingMap = {}
stt = 1

def gen():
    global stt
    pq = []
    heapq.heappush(pq, 1)
    while True:
        tmp = heapq.heappop(pq)
        hammingMap[tmp] = stt
        stt += 1
        if tmp >= 10 ** 18: break
        if tmp * 2 not in pq: heapq.heappush(pq, tmp * 2)
        if tmp * 3 not in pq: heapq.heappush(pq, tmp * 3)
        if tmp * 5 not in pq: heapq.heappush(pq, tmp * 5)


gen()
t = int(input())
for _ in range(t):
    n = int(input())
    if n in hammingMap: print(hammingMap[n])
    else: print("Not in sequence")