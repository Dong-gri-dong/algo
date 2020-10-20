T = int(input())

for test_case in range(1, T+1):
    # N 행의 개수 세로
    # M 열의 개수 가로
    # K 사각 테두리 한변의 길이
    N, M, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)] # 배열들을 받아준다.

    result = [] # 합의 결과들을 저장할것들
    for i in range(0, N-K+1):  # 세로축 돌릴수있는 횟수만큼

        for j in range(0, M-K+1): # 가로축 돌릴수있는 횟수만큼
            sums = 0 # 합을 잠시 저장할 변수
            for n in range(K): #가운데가 뚫려 있기때문에 이와같이 for문을 돌려줌
                if n == 0 or n == K-1: # 도너츠의 제일 상단과 하단은 모든 값이 다들어감
                    sums  += sum(arr[i + n][j:j + K])
                else: # 가운데 부분은 제일 좌측값과 우측값만 들어감
                    sums += arr[i + n][j] + arr[i + n][j+K-1]

            result.append(sums)  # 합을 배열에 추가 시켜줌

    print('#{} {}'.format(test_case, max(result) - min(result)))  # 거기서 최대값과 최소값을 구해서 출력값으로 사용함