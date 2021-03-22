import sys
sys.stdin = open("input_data/bj_10026_적록색약")

N = int(input())

arrs = [list(input()) for _ in range(N)]
dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]


# R == G

def bfs(y, x, RG):
    global num
    if visited[y][x] != 0:
        return
    Q = []
    Q.append([y, x])
    visited[y][x] = 1
    if arrs[y][x] in ['R', 'G']:
        if RG:
            color = ['R', 'G']
        else:
            color = arrs[y][x]
    else:
        color = arrs[y][x]
    num += 1
    while Q:
        y, x = Q.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx ==N or ty < 0 or ty == N:
                continue
            if arrs[ty][tx] not in color or visited[ty][tx] != 0:
                continue

            Q.append([ty, tx])
            visited[ty][tx] = 1


temp = [False, True]
for i in range(2):
    num = 0
    visited = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            bfs(y, x, temp[i])
    print(num, end=' ')


