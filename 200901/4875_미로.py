import sys

sys.stdin = open("input_data/4875.txt")

T = int(input())

dx =[ 0, 0, -1, 1]
dy =[-1, 1,  0, 0]

for test_case in range(1, T+1):
    flag = False
    N = int(input())

    visited = [[0] * N for _ in range(N)]
    G = [ list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if G[i][j] == 2:
                x = j
                y = i
                break




    visited[y][x] = 1
    S = [[y , x]]

    while S:
        if flag:
            break
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == N or ty < 0 or ty == N:
                continue
            if G[ty][tx] == 1 or visited[ty][tx] == 1:
                continue
            if G[ty][tx] == 3:
                flag = True
                break

            visited[ty][tx] = 1
            S.append([y,x])
            x = tx
            y = ty
            break

        else:
            x, y = S.pop()



    if flag:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(test_case, result))

