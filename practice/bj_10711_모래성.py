import sys
sys.stdin = open("input_data/bj_10711")

H, W = map(int, input().split())


arrs = [list(input()) for _ in range(H)]

for i in arrs:
    print(*i)



for i in range(H):
    for j in range(W):
        if arrs[i][j] == '.':
            arrs[i][j] = 0

# 상 하 좌 우 우상 좌상 우하 좌하
dx = [ 0, 0, -1, 1,  1, -1, 1, -1]
dy = [-1, 1,  0, 0, -1, -1, 1,  1]
visit = [ [0]*W for _ in range(H)]

# for i in visit:
#     print(*i)

def bfs(y, x):
    Q = []
    Q.append([y,x])
    visit[y][x] = 1
    while Q:
        count = 0
        y, x = Q.pop(0)

        for i in range(8):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == W or ty < 0 or ty == H:
                continue

            if  visit[ty][tx] != 0:
                continue

            if arrs[ty][tx] == 0:
                count += 1
            Q.append([ty,tx])
            visit[ty][tx] = 1
        if count > int(arrs[y][x]):
            arrs[y][x]= 0



for i in range(H):
    for j in range(W):
        visit = [[0] * W for _ in range(H)]
        bfs(i,j)

print(arrs)