import sys

sys.stdin = open("input_data/1249_보급로.txt")

from collections import deque
T = int(input())

dx = [0,  0, -1, 1]
dy = [-1, 1,  0, 0]
for test_case in range(1, T+1):
    N = int(input())
    arrs = [list(map(int, input())) for _ in range(N)]
    visited = [[3123123112] * N for _ in range(N)]

    y = 0
    x = 0
    Q = deque()
    Q.append((y,x))
    visited[y][x] = 0
    while Q:
        y, x = Q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx >= N or ty < 0 or ty >= N:
                continue

            if visited[y][x] + arrs[ty][tx] < visited[ty][tx]:
                visited[ty][tx]  = visited[y][x] + arrs[ty][tx]
                Q.append((ty, tx))


    print('#{} {}'.format(test_case, visited[N-1][N-1]))

