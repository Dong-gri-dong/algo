import sys

sys.stdin = open("input_data/1226.txt")


def DFS(x, y):
    global flag

    if flag:
        return

    visited[x][y] = 1
    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if tx < 0 or tx == N or ty < 0 or ty == N:
            continue
        if arr[tx][ty] == 1 or visited[tx][ty] == 1:
            continue
        if arr[tx][ty] == 3:
            flag = 1
        DFS(tx, ty)


def BFS(x, y):
    global flag
    Q = []

    Q.append([y,x])
    visited[y][x] = 1
    while Q:
        if flag:
            return
        y, x = Q.pop(0)
        #print(x, y)


        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == N or ty < 0 or ty == N:
                continue
            if arr[ty][tx] == 1 or visited[ty][tx] == 1:
                continue
            if arr[ty][tx] == 3:
                flag = 1
            Q.append([ty, tx])
            visited[ty][tx] = 1


dx = [ 0,  0, -1, 1]
dy = [-1,  1,  0, 0]

N = 16
for test_case in range(1, 11):
    _ = int(input())
    flag = 0
    arr = [ list(map(int, input())) for _ in range(N)]
    visited =[[0] * N for _ in range(N)]

    x = 1
    y = 1


    BFS(1, 1)
    print('#{} {}'.format(test_case, flag))