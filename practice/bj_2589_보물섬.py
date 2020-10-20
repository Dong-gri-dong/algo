import sys

sys.stdin = open("input_data/bj_2589")

from collections import deque
Y, X = map(int, input().split())

arr = [list(input()) for _ in range(Y)]


dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]


def bfs(y,x):
    if arr[y][x] == 'W':
        return
    Q = deque()
    Q.append([y, x])
    visit[y][x] = 1

    while Q:
        y, x = Q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx == X or ty < 0 or ty == Y:
                continue
            if arr[ty][tx] == 'W' or visit[ty][tx] != 0:
                continue
            Q.append([ty, tx])
            visit[ty][tx] = visit[y][x] + 1

def check():
    global maxs
    for i in visit:
        if maxs <= max(i):
            maxs = max(i)

maxs = 0
for y in range(Y):
    for x in range(X):
        visit = [[0] * X for _ in range(Y)]
        bfs(y, x)
        check()

print(maxs-1)

