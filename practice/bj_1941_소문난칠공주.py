import sys
from collections import deque
sys.stdin = open("input_data/bj_1941")

arr = [list(input()) for _ in range(5)]
visit = [[0] * 5 for _ in range(5)]

for i in arr:
    print(*i)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(y, x):
    S = []
    line = []
    S.append([y, x])
    visit[y][x] = 1
    while S:

        if len(line) == 7:
            print(line)
            pass

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == 5 or ty < 0 or ty == 5 or visit[ty][tx] == 1:
                continue
            S.append([y, x])
            line.append(arr[y][x])
            visit[ty][tx] = 1
            x = tx
            y = ty
            break

        else:
            y, x = S.pop()




dfs(1, 1)
