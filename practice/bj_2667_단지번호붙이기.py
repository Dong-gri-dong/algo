import sys
sys.stdin = open("input_data/bj_2667")




# 상하좌우
dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]

N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]


def dfs(y, x):
    global count
    global house
    if arr[y][x] == 0 or visit[y][x] == 1 :
        return
    S = []
    S.append([y,x])
    visit[y][x] = 1
    count += 1
    house += 1
    while S:

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == N or ty < 0 or ty == N:
                continue
            if arr[ty][tx] == 1 and visit[ty][tx] == 0:
                visit[ty][tx] = 1
                S.append([y,x])
                x = tx
                y = ty
                house += 1
                break
        else:
            y, x = S.pop()

count = 0
houses = []
for y in range(N):
    for x in range(N):
        house = 0
        dfs(y,x)
        if house:
            houses.append(house)


print(count)

houses = sorted(houses)
for i in houses:
    print(i)