import sys

sys.stdin = open("input_data/bj_5427")


T = int(input())
from collections import deque

def bfs(Q):
    while Q:
        y, x = Q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx == w or ty < 0 or ty == h:
                continue
            if arrs[ty][tx] == '#' or visit[ty][tx] != 0:
                continue

            Q.append([ty, tx])
            visit[ty][tx] = visit[y][x] + 1
            if tx == 0 or tx == w - 1 or ty == 0 or ty == h - 1:
                return visit[ty][tx]


def bfs_fire(Q_fire):
    while Q_fire:
        y, x = Q_fire.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx == w or ty < 0 or ty == h:
                continue
            if arrs[ty][tx] == '#' or visit_fire[ty][tx] != 0:
                continue

            Q_fire.append([ty, tx])
            visit_fire[ty][tx] = visit_fire[y][x] + 1

            if tx == 0 or tx == w - 1 or ty == 0 or ty == h - 1:
                return visit_fire[ty][tx]

#    동   서  남  북
dx = [1, -1, 0,  0]
dy = [0,  0, 1, -1]
for test_case in range(1, T+1):
    w, h = map(int, input().split())

    arrs = [list(input()) for _ in range(h)]

    visit_fire = [ [0]*w for _ in range(h)]
    visit = [[0] * w for _ in range(h)]






    Q = deque()
    Q_fire = deque()
    for y in range(h):
        for x in range(w):
            if arrs[y][x] == '@':
                Q.append([y,x])
                visit[y][x] = 1
            elif arrs[y][x] == '*':
                Q_fire.append([y,x])
                visit_fire[y][x] = 1



    a = bfs(Q)
    b = bfs_fire(Q_fire)

    if not a:
        print('IMPOSSIBLE')
    elif a < b:
        print(a)
    else:
        print('IMPOSSIBLE')