import sys
import pprint
sys.stdin = open('input_data/2806.txt')


def check_in(i, k, N):
    for j in range(N):
        arr[k][j] = 1
    for j in range(N):
        arr[j][i] = 1
    for j in range(N):
        if i+j == N or k+j == N:
            break
        else:
            arr[k+j][j+i] = 1

def check_out(i, k, N):
    for j in range(N):
        arr[k][j] = 0

    for j in range(N):
        arr[j][i] = 0

    for j in range(N):
        if i+j == N or k+j == N:
            break
        else:
            arr[k+j][j+i] = 0
    arr[i][k] = 1
T = int(input())
T = 1
for test_case in range(1, T+1):
    N = int(input())
    N = 5
    arr = [[0] * N for _ in range(N)]

    for i in arr:
        print(*i)
    print()
    def queen(k, N):
        global count
        if k == N:
            count += 1
            return
        else:
            for i in range(N):
                if arr[k][i] == 0:
                    check_in(i,k,N)
                    queen(k+1, N)
                    check_out(i, k, N)
                    for a in arr:
                        print(*a)
                    print()

    count = 0
    queen(0, N)
    print(count)




    #print('#{} {}'.format(test_case, count))





