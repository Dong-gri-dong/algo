import sys
sys.stdin = open("input_data/bj_7576_토마토")

M, N = map(int, input().split())

arrs = [ list(map(int, input().split())) for _ in range(N)]
dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]
visited = [[0] * M for _ in range(N)]

def bfs(y, x):
    Q = []
    Q.append([y, x])
    # visited[y][x] = 1

    while Q:
        y, x= Q.pop(0)

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == M or ty < 0 or ty == N:
                continue
            if visited[ty][tx] != 0 or arrs[ty][tx] == -1:
                continue


            visited[ty][tx] = visited[y][x] + 1





def check(arr):
    for i in arr:

        if i.count(0):
            return False

    return True
days = 0

while True:
    stop = True


    for y in range(N):
        for x in range(M):
            if days == 0:
                if arrs[y][x] == 1:
                    visited[y][x] = 1
                    stop = False
                    bfs(y, x)
            else:
                if visited[y][x] == days:
                    stop = False
                    bfs(y, x)


    if check(visited) or stop == True:
        break

    days += 1

if stop:
    print(-1)
else:
    print(days)