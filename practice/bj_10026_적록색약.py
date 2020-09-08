import sys

sys.stdin = open("input_data/bj_10026")

N = int(input())

dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]

G = [list(input()) for _ in range(N)]
visit1 = [[0] * N for _ in range(N)]
visit2 = [[0] * N for _ in range(N)]



def dfs(y,x):
    global count1
    if visit1[y][x] == 1:
        return

    S = []
    S.append([y,x])
    visit1[y][x] = 1
    color = G[y][x]
    count1 += 1

    while S:

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == N or ty < 0 or ty == N:
                continue
            if G[ty][tx] == color and visit1[ty][tx] == 0:
                visit1[ty][tx] = 1
                S.append([y,x])
                x = tx
                y = ty
                break
        else:
            y, x = S.pop()

def dfs_color(y,x):
    global count2
    if visit2[y][x] == 1:
        return

    S = []
    S.append([y,x])
    visit2[y][x] = 1

    if G[y][x] == 'G' or G[y][x] == 'R':
        color = ['G', 'R']
    else:
        color = ['B']

    count2 += 1

    while S:

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == N or ty < 0 or ty == N:
                continue
            if G[ty][tx] in color and visit2[ty][tx] == 0:
                visit2[ty][tx] = 1
                S.append([y,x])
                x = tx
                y = ty
                break
        else:
            y, x = S.pop()



count1 = 0
count2 = 0
for y in range(N):
    for x in range(N):
        dfs(y, x)
        dfs_color(y, x)





print('{} {}'.format(count1, count2))
