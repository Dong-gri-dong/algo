import sys

sys.stdin = open('input_data/1979.txt')



T = int(input())


for test_case in range(1, T+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]



    final_count = 0
    for i in range(N):
        count = 0
        for k in range(N):
            if arr[i][k] == 1:
                count += arr[i][k]
            else:
                if count == K:
                    final_count += 1
                count = 0

        if count == K:
            final_count += 1


    for k in range(N):
        count = 0
        for i in range(N):
            if arr[i][k] == 1:
                count += arr[i][k]
            else:
                if count == K:
                    final_count += 1
                count = 0

        if count == K:
            final_count += 1

    print('#{} {}'.format(test_case, final_count))

