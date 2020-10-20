import sys
sys.stdin = open("input_data/bj_2468")

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]




dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y,x, H):
    global count
    if visit[y][x] == 1 or arr[y][x] <= H:
        return
    Q = []
    Q.append([y, x])
    visit[y][x] = 1
    count += 1
    while Q:
        y, x = Q.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx ==N or ty < 0 or ty == N:
                continue
            if visit[ty][tx] == 1 or arr[ty][tx] <= H:
                continue
            Q.append([ty, tx])
            visit[ty][tx] = 1



max_h = 0
for i in arr:
    value = max(i)
    if max_h < value:
        max_h = value

result = 0

for H in range(0, max_h+1):
    count = 0
    visit = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            bfs(y, x, H)
    if result <= count:
        result = count

print(result)