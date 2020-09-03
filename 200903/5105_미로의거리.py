import sys

sys.stdin = open("input_data/5105.txt")

T = int(input())

# 상 하 좌 우
dx =[ 0, 0, -1, 1]
dy =[-1, 1,  0, 0]

for test_case in range(1, T+1):
    N = int(input())

    G = [list(map(int, input())) for _ in range(N)]


    visit = [ [0] * N for _ in range(N)]


    def bfs(y, x):
        Q = []

        Q.append([y,x])
        visit[y][x] = 1

        while Q:
            y, x = Q.pop(0)

            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]

                if tx < 0 or tx == N or ty < 0 or ty == N:
                    continue
                if G[ty][tx] == 1 or visit[ty][tx] != 0:
                    continue

                Q.append([ty, tx])
                visit[ty][tx] = visit[y][x] + 1
                if G[ty][tx] == 3:
                    return visit[ty][tx]-2


    for i in range(N):
        for k in range(N):
            if G[i][k] == 2:
                y = i
                x = k
                break

    result = bfs(y, x)
    if result:
        print('#{} {}'.format(test_case, result))
    else:
        print('#{} {}'.format(test_case, 0))

