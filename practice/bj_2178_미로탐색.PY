import sys

sys.stdin = open("input_data/bj_2178_미로탐색")

N, M = map(int, input().split())

G = [list(map(int, input())) for _ in range(N) ]
visit = [ [0] * (M) for _ in range(N) ]



dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]

def BFS(y,x):
    Q = []
    Q.append([y, x])
    visit[y][x] = 1

    while Q:
        y, x =Q.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx == M or ty < 0 or ty == N:
                continue
            if visit[ty][tx] != 0 or G[ty][tx] != 1:
                continue
            Q.append([ty, tx])
            visit[ty][tx] = visit[y][x] + 1

BFS(0, 0)
print(visit[N-1][M-1])




