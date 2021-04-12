import sys
sys.stdin = open("./input/16234_인구이동")

dx = [0,  0, -1, 1]
dy = [-1, 1,  0, 0]

# N 땅크기
# 인구차이 L명 이상 R명 이하
N, L, R = map(int, input().split())

arrs = [list(map(int, input().split())) for _ in range(N)]

temp =[]




def bfs(y,x):
    temp = []
    Q = []

    if visit[y][x] != 0:
        return
    Q.append([y, x])
    visit[y][x] = 1


    while Q:
        y, x = Q.pop(0)
        temp.append([y, x])
        # print(temp)

        for i in range(4):

            tx = x + dx[i]
            ty = y + dy[i]


            if tx < 0 or N <= tx or ty < 0 or N <= ty:
                continue
            if visit[ty][tx] != 0:
                continue
            if  L <= abs(arrs[y][x]-arrs[ty][tx]) <=R:
                Q.append([ty, tx])
                visit[ty][tx] = 1
            else:
                continue


    return temp


visit = [[0] * N for _ in range(N)]
keep = []
n = 0
while True:

    for i in arrs:
        print(*i)

    keep = []
    visit = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            a = bfs(y, x)
            if a and len(a) > 1:
                keep.append(a)
    print(keep)
    if not keep:
        break
    n += 1
    sums = 0

    for i in range(len(keep)):
        for y, x in keep[i]:
            sums += arrs[y][x]
        change = int(sums/len(keep[i]))

        for y, x in keep[i]:
            arrs[y][x] = change



print(n)








