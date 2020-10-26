T = int(input())  # 테스트 케이스 수

def rotate(arr, C, K): # 회전 함수
    rotate_num = C // 90 # 회전 횟수
    center = [K // 2, K // 2] # 배열 중심 좌표
    j = 0  # 몇번 돌릴지에 대한 정보
    while j < rotate_num: # 몇번회전에 대한 조건
        new = [[0] * K for _ in range(K)] # 돌린 값을 담을 배열
        for Y in range(K):  # 들어오는 배열을 한번씩 봄
            for X in range(K):
                new[center[0] - (center[1] - X)][center[1] + (center[0] - Y)] = arr[Y][X]
                # 회전할때 90도를 기준으로 위치가 그 점에서 중심기준으로
                # 새로운 y좌표는 y중심좌표 - (x중심좌표-현재 x좌표)이고
                # 새로운 x좌표는 x중심좌표 + (y중심좌표-현재 y좌표)이다.
        j += 1  # 한번 회전하면 횟수올림
        arr = new[:] # arr를 배열을 바꿔줌 (돌린거를 넘겨주는 역할)
    return arr

for test_case in range(1, T+1):
    # N: 배열의 크기
    # C: 회전 각도
    # x, y: 시작 위치
    # K: 부분 영역의 가로세로 값
    # R: 출력 행
    N, C, x, y, K, R = map(int, input().split())

    arrs = [list(map(int, input().split())) for _ in range(N)] # 배열 받기


    if x + (K-1) > N or y+ (K-1) > N:  # 범위에서 벗어났을때 -1을 출력해주기 위한 조건문
        print('#{} -1'.format(test_case))
        continue

    # 좌표가 0시작이아니라 1시작이여서 편하게 해주기 위해 해줌
    x -= 1
    y -= 1

    # 그 돌릴부분만 얻기위한 부분
    new_arrs = []
    for Y in range(y, y+K):
        temp = []
        for X in range(x, x+K):
            temp.append(arrs[Y][X])
        new_arrs.append(temp)


    new = rotate(new_arrs, C, K) # 함수를 써서 돌림
    for Y in range(y, y+K):
        for X in range(x, x+K):
            arrs[Y][X] = new[Y-y][X-x] # 돌린값을 원래 배열에 넣어줌


    print('#{} {}'.format(test_case, sum(arrs[R-1])))





