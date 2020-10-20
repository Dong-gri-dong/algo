# bfs 함수 작성
def bfs(y, x):
    global count #폭탄의 수를 받을 변수
    Q = [] # Queue를 만들어주고
    Q.append([y, x]) # en q를 하고
    visit[y][x] = 1 # 방문행렬에 추가

    while Q: # Q가 빌때까지

        y, x = Q.pop(0)  # Q에서 pop해준값으로 y와 x를 사용
        for i in range(4): # 상하 좌우 인데 폭탄의 범위만큼 가야하므로
            for j in range(1, arr[y][x] + 1): # 다음과 같이 for문을 통해 범위만큼 가게 함
                tx = x + dx[i] * j
                ty = y + dy[i] * j

                # 여기 두 조건은 불가능 할때의 조건
                if tx < 0 or tx >= N or ty < 0 or ty >= N: # 범위를 벗어났을때
                    continue
                if arr[ty][tx] == 0 or visit[ty][tx] != 0: # 폭탄이 없거나 방문을 했을때
                    continue

                Q.append([ty, tx]) # 위에 조건에 안걸리면 가능한것이므로 다음과 같이 en q
                visit[ty][tx] = 1 # 그리고 방문행렬 굳이 거리를 안구해도 되므로 1로만 해도 됨

                count += 1 # 폭탄의 수를 추가해줌
T = int(input())

# 상하 좌우
dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]
for test_case in range(1, T+1):
    # N 지도의 크기
    N = int(input())
    # boom 폭발 위치
    boom = list(map(int, input().split()))

    # 지도 배열을 받아준다.
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 방문 행렬만들기
    visit = [[0] * N for _ in range(N)]


    count = 1 # 첫번째 터지는 폭탄을 포함 해야하므로 1부터 시작
    bfs(boom[0], boom[1]) # bfs 함수를 불러온다
    print('#{} {}'.format(test_case, count)) # 출력
