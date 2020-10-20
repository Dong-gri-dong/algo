import sys
sys.stdin = open("input_data/bj_1726")


# 세로 가로
M, N  = map(int, input().split())

arrs = [list(map(int, input().split())) for _ in range(M)]



start_y, start_x, start_direct = map(int, input().split())
end_y, end_x, end_direct = map(int, input().split())



visit = [ [0] * N for _ in range(M)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
    Q = []
    Q.append([y,x])

    visit[y][x] = 1

    while Q:
        y, x = Q.pop(0)

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or tx == N or ty < 0 or ty == M:
                continue
            if arrs[ty][tx] == 1 or visit[ty][tx] != 0:
                continue
            Q.append([ty, tx])
            visit[ty][tx] = visit[y][x] + 1



start_y -= 1
start_x -= 1

end_y -= 1
end_x -= 1

print(start_y, start_x)
bfs(start_y, start_x)

for i in arrs:
    print(*i)
print()
for i in visit:
    print(*i)