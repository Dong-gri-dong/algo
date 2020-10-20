import sys
sys.stdin = open("input_data/bj_2583")

def nemo(x1, y1, x2, y2):
    for y in range(y1, y2):
        for x in range(x1, x2):
            arr[y][x] = 0

M, N, K = map(int, input().split())

temp = [list(map(int, input().split())) for _ in range(K)]
# [0] [1] : 왼쪽 아래 x, y 좌표
# [2] [3] : 오른쪽 위 x, y 좌표
arr = [[1] * N for _ in range(M)]
visit = [[0] * N for _ in range(M)]

for i in temp:
    nemo(i[0], i[1], i[2], i[3])


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y,x):
    global count
    global size
    if arr[y][x] == 0 or visit[y][x] == 1:
        return
    Q = []
    Q.append([y,x])
    visit[y][x] = 1
    count += 1

    while Q:
        y, x = Q.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == N or ty < 0 or ty == M:
                continue
            if visit[ty][tx] == 1 or arr[ty][tx] == 0:
                continue
            Q.append([ty, tx])
            visit[ty][tx] = 1
            size += 1
    S.append(size)
count = 0
S = []
for y in range(M):
    for x in range(N):
        size = 1
        bfs(y, x)

print(count)
for i in sorted(S):
    print(i, end =' ')


