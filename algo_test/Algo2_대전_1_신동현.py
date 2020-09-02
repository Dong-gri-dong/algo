T = int(input()) # test_case 수를 받음

#     상  하  좌  우
dx = [ 0, 0, -1, 1]
dy = [-1, 1,  0, 0]

for test_case in range(1, T+1):
    # M : 마당의 가로길이
    # N : 마당의 세로길이
    # K : 연못 좌표 개수
    M, N, K = map(int, input().split())

    # 일단 가로 M 세로 N의 0으로 채운 마당 배열과 방문 배열을 만들어줌
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]


    V = [] # 물고기수(즉, 연결요소?이름이 정확히 기억이 안납니다...)를 찾기 위한 인풋값들을 받기 위한 list

    for i in range(K): # 좌표 개수만큼 for문을 돌림
        s, e = map(int, input().split())
        # 여기서 e와 s를 거꾸로 준 이유는  문제에서는 앞의 숫자가 가로이기 때문 파이썬에서는 앞 숫자가 세로를 의미 ex 1행 2행 ...
        V.append([e, s])
        arr[e][s] = 1 # 연못좌표를 넣어줌


    S = []  # stack을 만들어줌
    count = 0 #물고기수를 셀 변수

    for v in V:  #위에서 설정한 변수 그냥 MxN만큼 전체의 index를 넣어줘도될듯한데 먼가 비효율적이라고 생각해서 이렇게 넣음
        y, x = v  # 시작 포인트를 x와 y에 넣어줌

        if visited[y][x]: # 만약에 방문한지점이면 굳이 할 필요없기 때문에 다음으로 넘겨줌
            continue

        visited[y][x] = 1  # 방문했다고 기록
        S.append([y,x])    # stack에도 넣어줌

        while S:  # stack이 빌때까지 반복

            for i in range(4): # 상하좌우 탐색
                tx = x + dx[i]
                ty = y + dy[i]

                # 아래 조건문은 불가능한 경우일때(연못을 넘어갈때)
                if tx < 0 or tx == M or ty < 0 or ty == N:
                    continue
                # 아래 조건문은 연못이 아니거나 방문을 했을때의 경우는 필요없기 때문에 넘어가는 if문
                if arr[ty][tx] == 0 or visited[ty][tx] == 1:
                    continue

                visited[ty][tx] = 1  #방문 했다고 알림
                S.append([y,x]) # stack 추가해줌
                # tx와 ty로 이동
                x = tx
                y = ty

                break
            # for else 구문은 break가 안나오면 else를 출력
            else:
                y, x = S.pop()  # 연결된 연못이 없기때문에 pop을하므로써 다시 돌아감

        count += 1 # 물고기 수를 세줌

    print('#{} {}'.format(test_case, count)) # 결과값 출력