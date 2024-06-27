from collections import deque

# Mảng dx và dy mô tả 8 hướng di chuyển
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

def BFS(sx, sy, ex, ey, marked_point):
    q = deque()
    q.append((sx, sy, 0))  # Hàng đợi lưu điểm và số bước di chuyển đến điểm đó
    visited = set()
    visited.add((sx, sy))

    while q:
        ux, uy, step = q.popleft()
        if ux == ex and uy == ey: return step
        for i in range(8):
            ox, oy = ux + dx[i], uy + dy[i]
            if (ox, oy) in marked_point and (ox, oy) not in visited:
                visited.add((ox, oy))
                q.append((ox, oy, step + 1))
    return -1

for _ in range(int(input())):
    sx, sy, ex, ey = map(int, input().split())
    n = int(input())
    marked_point = set()
    for i in range(n):
        x, y1, y2 = map(int, input().split())
        for y in range(y1, y2 + 1): marked_point.add((x, y))

    if (sx, sy) not in marked_point or (ex, ey) not in marked_point: print(-1)
    else:
        result = BFS(sx, sy, ex, ey, marked_point)
        print(result)

