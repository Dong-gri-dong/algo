import sys
import pprint
sys.stdin = open('input_data/2806.txt')


def check_in(i, k, N):
    for j in range(N):
        arr[k][j] = 1
    for j in range(N):
        arr[j][k] = 1

    for j in range(N):
        if i+j == N or k+j == N:
            break
        else:
            arr[i+j][i+k] = 1


T = int(input())
T = 1
for test_case in range(1, T+1):
    N = int(input())
    N = 5
    arr = [[0] * N for _ in range(N)]

    for i in arr:
        print(*i)

    def queen(k, N):
        if k == N:
            return
        else:
            for i in range(N):
                if arr[k][i] == 0:
                    check_in(i, k, N)
                    for i in arr:
                        print(*i)
                    queen(k+1, N)

    queen(0, N)




    #print('#{} {}'.format(test_case, count))





