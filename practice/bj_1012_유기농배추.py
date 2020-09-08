import sys

sys.stdin = open("input_data/bj_1012")


def dfs(y, x):
    global count
    if G[y][x] == 0 or visit[y][x] == 1:
        return
    S = []
    S.append([y, x])
    visit[y][x] = 1
    count += 1

    while S:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == M or ty < 0 or ty == N:
                continue
            if G[ty][tx] == 1 and visit[ty][tx] == 0:
                visit[ty][tx] = 1
                S.append([y, x])
                x = tx
                y = ty
                break
        else:
            y, x = S.pop()

T = int(input())

dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]
for test_case in range(1, T+1):
    M, N, K = map(int, input().split())

    G = [[0] * M for _ in range(N)]
    visit = [[0] * M for _ in range(N)]

    points = []
    for i in range(K):
        e, s = map(int, input().split())
        G[s][e] = 1
        points.append([e,s])



    count = 0
    for y in range(N):
        for x in range(M):
            dfs(y, x)
    print(count)