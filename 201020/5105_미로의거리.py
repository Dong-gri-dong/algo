import sys
sys.stdin = open("input_data/5105_미로의거리.txt")


T = int(input())


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(y, x):
    global flag
    Q = []
    Q.append([y, x])
    visit[y][x] = 1

    while Q:
        if flag:
            return

        y, x = Q.pop(0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == N or ty < 0 or ty == N:
                continue
            if visit[ty][tx] != 0 or arrs[ty][tx] == 1:
                continue

            Q.append([ty, tx])
            visit[ty][tx] = visit[y][x] + 1
            if arrs[ty][tx] == 2:
                flag = True

for test_case in range(1, T+1):
    flag = False
    N = int(input())

    arrs = [list(map(int, input())) for _ in range(N)]


    for y in range(N):
        for x in range(N):
            if arrs[y][x] ==3:
                start = [y,x]
            elif arrs[y][x] ==2:
                end = [y, x]

    visit = [[0]* N for _ in range(N)]
    bfs(start[0], start[1])



    if flag:
        print('#{} {}'.format(test_case, visit[end[0]][end[1]]-2))
    else:
        print('#{} 0'.format(test_case))
