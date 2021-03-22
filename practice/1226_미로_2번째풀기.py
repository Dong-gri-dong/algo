import sys

sys.stdin = open("input_data/1226.txt")


def bfs(y, x):
    global flag
    Q = []
    Q.append([y, x])
    visited[y][x] = 1

    while Q:
        if flag:
            return
        y, x = Q.pop(0)

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == N or ty < 0 or ty == N:
                continue
            if arrs[ty][tx] == 1 or visited[ty][tx] == 1:
                continue
            if arrs[ty][tx] == 3:
                flag = 1

            Q.append([ty, tx])
            visited[ty][tx] = 1




dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]

N = 16
for i in range(0, 10):
    flag = 0
    T = int(input())

    arrs = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    bfs(2,2)


    print('#{} {}'.format(T, flag))