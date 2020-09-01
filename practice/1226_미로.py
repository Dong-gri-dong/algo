import sys

sys.stdin = open("input_data/1226.txt")




dx = [ 0,  0, -1, 1]
dy = [-1,  1,  0, 0]

N = 16
for test_case in range(1, 10+1):
    _ = int(input())
    flag = 0
    arr = [ list(map(int, input())) for _ in range(N)]
    visited =[[0] * N for _ in range(N)]



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

    def dfs(s):
        visited[v] = 1
        for i in range(1, N+1):
            if G[v][w] == 1 and visited == 0:
                dsf(w)

    DFS(1, 1)
    print('#{} {}'.format(test_case, flag))