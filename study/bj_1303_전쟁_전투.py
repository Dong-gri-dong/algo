import sys
sys.stdin = open("input_data/bj_1303_전쟁_전투")
N, M = map(int, input().split())

dx = [0,  0, -1, 1]
dy = [-1, 1,  0, 0]

arrs = [list(input()) for _ in range(M)]




visit = [[0]* N for _ in range(M)]
visit_b = [[0]* N for _ in range(M)]
def bfs(y,x):
    global result
    if visit[y][x] != 0 or arrs[y][x] == 'B':
        return
    result += 1
    Q = []
    Q.append([y,x])
    visit[y][x] = 1

    while Q:
        y, x = Q.pop(0)
        for i in range(4):
            tx = dx[i] + x
            ty = dy[i] + y
            if tx < 0 or tx == N or ty < 0 or ty == M:
                continue
            if visit[ty][tx] != 0 or arrs[ty][tx] == 'B':
                continue
            Q.append([ty, tx])
            visit[ty][tx] = visit[y][x] + 1
            result += 1

def bfs_b(y,x):
    global result_b
    if visit_b[y][x] != 0 or arrs[y][x] == 'W':
        return
    result_b += 1
    Q = []
    Q.append([y,x])
    visit_b[y][x] = 1

    while Q:
        y, x = Q.pop(0)
        for i in range(4):
            tx = dx[i] + x
            ty = dy[i] + y
            if tx < 0 or tx == N or ty < 0 or ty == M:
                continue
            if visit_b[ty][tx] != 0 or arrs[ty][tx] == 'W':
                continue
            Q.append([ty, tx])
            visit_b[ty][tx] = visit_b[y][x] + 1
            result_b += 1


result = 0
result_b = 0
final = []
final_b = []
for y in range(M):
    for x in range(N):
        bfs(y, x)
        if result:
            final.append(result)
            result = 0
        bfs_b(y, x)
        if result_b:
            final_b.append(result_b)
            result_b = 0




result = 0
result_b = 0
for i in final:
    result += i**2
for i in final_b:
    result_b += i**2
print(result, result_b)

