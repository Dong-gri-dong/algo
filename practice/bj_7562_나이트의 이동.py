import sys

sys.stdin = open("input_data/bj_7562")


from collections import deque
T = int(input())


dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for test_case in range(1, T+1):
    I = int(input())
    s = list(map(int, input().split()))
    e = list(map(int, input().split()))

    def bfs(y,x):
        global flag
        global result
        if s[0] == e[0] and s[1] == e[1]:
            return

        Q = deque()
        Q.append([y,x])
        visit[y][x] = 1
        while Q:
            if flag:
                result = visit[e[0]][e[1]]-1
                return
            y, x = Q.popleft()
            for i in range(8):
                tx = x + dx[i]
                ty = y + dy[i]

                if 0<= tx <I and 0<= ty <I and visit[ty][tx] ==0:
                    Q.append([ty, tx])
                    visit[ty][tx] = visit[y][x] + 1
                    if ty == e[0] and tx ==e[1]:
                        flag = True
    result = 0
    flag = False
    visit = [[0] * I for _ in range(I)]
    bfs(s[0], s[1])
    print(result)




