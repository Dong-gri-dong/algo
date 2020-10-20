import sys
from collections import deque

sys.stdin = open("input_data/bj_7576")

M, N = map(int, sys.stdin.readline().split())

# arr = [list(map(int, input().split())) for _ in range(N)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visit = [[0] * M for _ in range(N)]




dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]


def bfs(y, x):
    if arr[y][x] == 0:
        return
    global day
    Q = deque()
    Q.append([y,x])
    visit[y][x] = 1
    while Q:

        y, x = Q.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == M or ty < 0 or ty == N or visit == -1:
                continue

            visit[ty][tx] = visit[y][x] + 1
            Q.append([ty, tx])


        count = 0
        for i in visit:
            if 0 in i:
                break
        else:
            day = visit[ty][tx]
            return
day = 0
for y in range(N):
    for x in range(M):
        bfs(y, x)

print(day-1)

# import sys
# from collections import deque
#
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# def bfs(M, N, visit):
#
#     day = -1
#
#     while Q:
#         day += 1
#         for _ in range(len(Q)):
#             y, x = Q.popleft()
#
#             for i in range(4):
#                 tx = x + dx[i]
#                 ty = y + dy[i]
#
#                 if (0<= tx < M) and (0 <= ty < N) and (visit[ty][tx] == 0):
#                     visit[ty][tx] = visit[y][x] + 1
#                     Q.append([ty,tx])
#     for b in visit:
#         if 0 in b:
#             return -1
#     return day
#
#
#
# M, N = map(int, sys.stdin.readline().split())
# Q, visit = deque(), []
# for y in range(N):
#     row = list(map(int, sys.stdin.readline().split()))
#     for x in range(M):
#         if row[x] == 1:
#             Q.append([y,x])
#     visit.append(row)
#
# print(bfs(M, N, visit))