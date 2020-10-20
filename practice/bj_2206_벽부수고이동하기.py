import sys

sys.stdin = open("input_data/bj_2206")

# 상 하 좌 우
dx = [0,  0, -1, 1]
dy = [-1, 1,  0, 0]

N, M = map(int, input().split())

arrs = [list(map(int, input())) for _ in range(N)]



visit = [[0]*(M) for _ in range(N)]




def bfs(y,x , count):
    global flag
    Q = []
    Q.append([y, x, count])
    visit[y][x] = 1


    while Q:
        if flag:
            break

        y, x, count = Q.pop(0)

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx == M or ty < 0 or ty == N:
                continue

            if visit[ty][tx] != 0:
               continue

            if count == 1 and arrs[ty][tx] == 1:
                continue

            if count == 0 and arrs[ty][tx] == 1:
                count = 1

                Q.append([ty, tx, count])
                visit[ty][tx] = visit[y][x] + 1
                count = 0
                continue
            Q.append([ty, tx, count])
            visit[ty][tx] = visit[y][x] + 1

            if tx == M-1 and ty == N-1:
                flag = True
                break



flag = False
count = 0
bfs(0, 0, count)

# for i in visit:
#     print(*i)

if visit[N-1][M-1]:
    print(visit[N-1][M-1])
else:
    print(-1)


arr = [[[1,2,3], [4,5,6]] , [[7,8, 9], [10, 11, 12]]]
print(arr)
print((arr[0][1][2]))