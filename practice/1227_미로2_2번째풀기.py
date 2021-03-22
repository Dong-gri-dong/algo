import sys
import pprint

sys.stdin = open("input_data/1227.txt")

N = 100
dx = [ 0, 0,-1, 1]
dy = [-1, 1, 0, 0]
for test_case in range(1, 11):
    flag = 0
    T = int(input())

    arrs = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    def BFS(y,x):
        global flag
        Q = []
        Q.append([y,x])
        visited[y][x] = 1

        while Q:
            if flag:
                return
            y,x = Q.pop(0)

            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]

                if tx < 0 or tx == N or ty < 0 or ty == N:
                    continue
                if arrs[ty][tx] == 1 or visited[ty][tx] != 0:
                    continue
                if arrs[ty][tx] == 3:
                    flag = 1
                Q.append([ty, tx])
                visited[ty][tx] = visited[y][x] + 1

    BFS(2,2)


    print('#{} {}'.format(T, flag))