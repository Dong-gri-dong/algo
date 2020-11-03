import sys
sys.stdin = open("input_data/bj_1743_음식물피하기")
N, M, K = map(int, input().split())


arrs = [ [0] * (M+1) for _ in range(N+1)]

dx = [0,  0, -1, 1]
dy = [-1, 1,  0, 0]

temp = [ list(map(int, input().split())) for _ in range(K)]
for i in range(K):
    a, b = temp[i]
    arrs[a][b] = 1

visit = [ [0] * (M+1) for _ in range(N+1)]



def bfs(y,x):
    global result
    if visit[y][x] != 0 or arrs[y][x] == 0:
        return
    result = 1
    Q = []
    Q.append([y,x])
    visit[y][x] = 1

    while Q:

        y, x = Q.pop(0)
        for i in range(4):
            tx = dx[i] + x
            ty = dy[i] + y

            if tx < 0 or tx >= M+1  or ty < 0 or ty >= N+1:
                continue
            if visit[ty][tx] != 0 or arrs[ty][tx] == 0:
                continue

            Q.append([ty, tx])
            visit[ty][tx] = visit[y][x] + 1
            result += 1



maxs = 0
for i in temp:
    y, x = i
    bfs(y, x)
    if maxs <= result:
        maxs = result



print(maxs)