T = int(input())  # Test_case의 수

for test_case in range(1, T+1):
    # N : 배열의 크기
    # M : 첫번째 입력값
    # D : 변경 값
    N, M, D = map(int, input().split())  # 위에 해당하는 input들을 받음


    arr = [[0] * N for _ in range(N)]  # NxN의 0으로된 배열을 만들어줌

    center = N//2  # NxN 배열의 가운데 index

    loops = N - center
    # for 문을 돌려서 배열을 채울것인데 그때 for문을 돌릴횟수

    for n in range(loops):
        # 중심을 기준으로 좌측과 우측으로 값을 채워넣기위한 변수
        x = center - n
        y = center + n

        # 배열의 값을 집어 넣기 위한 for문
        for i in range(x, y+1):
            for j in range(x, y+1):
                # 여기서 중심부터 채워넣는데 안에 값이 있으면(즉, 0이 아님) 채워넣지 않고
                # 값이 없으면(즉, 0이면) 채워넣는다.
                if arr[i][j]:
                    pass
                else:
                    arr[i][j] = M  # M은 초기값 부터 시작해 아래의 식처럼 변경값 D를 이용해 바꾸어 나간다.

        M += D  # 배열안에 넣어줄 값을 초기값 M과 변경값D 를 이용해 바꾸어 준다.

    # 여기서 부터 결과 출력
    print('#{}'.format(test_case), end =' ')  # test_case즉 '#1'과 같은 값을 출력해준다.
    for i in range(N): #for문을 돌면서 배열의 합을 출력해줌
        print('{}'.format(sum(arr[i])), end=' ')
    print()
