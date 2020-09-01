import sys
import pprint

sys.stdin = open("input_data/1227.txt")


dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]
N = 100
for test_case in range(1, 11):
    flag = False
    _ = int(input())

    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]


    x = 1
    y = 1
    visited[x][y] = 1
    S = [[x,y]]

    while S:

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == N or ty < 0 or ty == N:
                continue
            if arr[tx][ty] == 1 or visited[tx][ty] == 1:
                continue
            if arr[tx][ty] == 3:
                flag = True

            visited[tx][ty] = 1
            S.append([tx, ty])
            x = tx
            y = ty
            break

        else:
            x, y = S.pop()




    # for i in visited:
    #     print(*i)
    result = 0
    if flag:
        result = 1

    print('#{} {}'.format(test_case, result))