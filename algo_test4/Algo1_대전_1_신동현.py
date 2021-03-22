


T = int(input())

for test_case in range(1, T+1):
    # N 은 지도 크기
    # M 은 폭탄의 수
    N, M = map(int, input().split())

    # 지도
    arrs = [ list(map(int, input().split())) for _ in range(N)]

    # 폭탄 정보
    boom = [list(map(int, input().split())) for _ in range(M)]

    # 범위의 리스트를 뽑아내는 함수 여기서 info는 폭탄정보
    def boom_check(info):
        boom_list = [] # 리스트를 담을 변수
        # for문은 NxN지도를 보는 for문
        for y in range(N):
            for x in range(N):
                if y == info[0]: # y 가 같으면
                    if abs(info[1]-x) <= info[2]: # 폭탄위치를 기준으로 x축이 폭발력보다 안크면 폭탄 범위
                        boom_list.append([y, x])
                else:
                    if x == info[1]: # x가 같으면  # 폭탄위치를 기준으로 y축이 폭발력보다 안크면 폭탄 범위
                        if abs(info[0] - y) <= info[2]:
                            boom_list.append([y, x])

        return boom_list


    temp = [] # 전체 폭파되는 리스트를 담을 변수
    for i in boom: # 폭탄 정보를 하나씩 받아서
        temp.extend(boom_check(i)) # 리스트에 받아줌


    result = 0 # 최종 결과값
    for i in temp: # 받은 리스트를 하나씩 순회
        y, x = i
        result += arrs[y][x] # 값을 더해줌
        arrs[y][x] = 0 # 근데 중복이 있을수도 있어서 그 지점을 0 으로 바꿔서 중복이여도 값에 영향이없게 해줌

    print('#{} {}'.format(test_case, result))
