import sys
import pprint
sys.stdin = open('input_data/2806.txt')

T = int(input())




for test_case in range(1, T+1):

    N = int(input())
    N = 5
    arr = [ [0] * N for _ in range(N)]
    #visit = [[0] * N for _ in range(N)]
    visit = [0] * N

    def queen(k, N):

        global count
        if k == N:
            count += 1

        else:
            for i in range(N):
                if visit[i] == 0:
                    visit[i] = 1
                    visit[i+k] = 1
                    queen(k+1, N)
                    visit[i] = 0
                    visit[i - k] = 0



    count = 0



    queen(0, N)


    print('#{} {}'.format(test_case, count))





