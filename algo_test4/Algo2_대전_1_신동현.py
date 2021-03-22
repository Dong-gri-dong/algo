import sys
sys.stdin = open("input_data/algo2")

T = int(input())

#     상  하  좌  우
dx = [0,  0, -1, 1]
dy = [-1, 1,  0, 0]
for test_case in range(1, T+1):
    # 미로 크기
    N = int(input())

    # 미로 정보
    arrs = [list(map(int, input())) for _ in range(N)]

    # 출발점과 도착점을 찾는 for 문
    for y in range(N):
        for x in range(N):
            if arrs[y][x] == 2:
                start = [y,x]
            if arrs[y][x] == 3:
                end = [y,x]

    # visit은 방문 행렬
    visit = [[0]*N for _ in range(N)]

    # check는 벽을 제거 했는지를 체크할 행렬
    check = [[0] * N for _ in range(N)]

    # bfs를 사용
    def bfs(y, x):
        global result # 최종 결과를 담을 변수
        Q = [] # q를 만들어 주고
        Q.append([y, x]) # en Q
        visit[y][x] = 1 # 방문 체크

        while Q: # q가 빌때 까지

            y, x = Q.pop(0)
            for i in range(4): # 상하좌우
                tx = x + dx[i]
                ty = y + dy[i]

                if tx < 0 or tx >= N or ty < 0 or ty >= N: # 범위를 넘으면 continue
                    continue
                if visit[ty][tx] != 0: # 방문한곧이면 continue
                    continue
                if  arrs[ty][tx] == 1 and check[y][x] == 1: # 벽인데 벽을 이미 제거했으면 못가므로 continue
                    continue
                elif arrs[ty][tx] == 1 and check[y][x] == 0: # 벽인데 벽을 이전에 제거 안했으면 체크하고 뚫고 감
                    check[ty][tx] = 1

                Q.append([ty, tx])  # q에 넣어줌
                visit[ty][tx] = visit[y][x] + 1 # 방문체크를 하는데 경로 몇번했는지를 알아야하므로

                if arrs[ty][tx] == 3: # 도착점에 도착했으면 종료
                    result = visit[ty][tx]
                    return

    y, x = start
    result = 0

    bfs(y,x)

    y, x = end

    print('#{} {}'.format(test_case, result))

