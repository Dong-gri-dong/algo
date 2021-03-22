import sys
sys.stdin = open("input_data/bj_2667_단지번호붙이기")

N = int(input())

arrs = [list(map(int,input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]



dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]

def bfs(y, x):
    global totals
    if arrs[y][x] == 0 or visited[y][x] != 0:
        return
    totals += 1
    Q = []
    Q.append([y, x])
    visited[y][x] = 1
    num = 1
    while Q:
        y, x = Q.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == N or ty < 0 or ty == N:
                continue
            if visited[ty][tx] != 0 or arrs[ty][tx] == 0:
                continue

            Q.append([ty, tx])
            visited[ty][tx] = visited[y][x] + 1
            num += 1
    dangis.append(num)



totals = 0
dangis = []

for y in range(N):
    for x in range(N):
        bfs(y, x)

print(totals)
for i in sorted(dangis):
    print(i)