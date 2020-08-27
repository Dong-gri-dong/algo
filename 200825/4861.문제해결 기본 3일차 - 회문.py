import sys
import pprint
sys.stdin = open('input_data/4861.txt')

T = int(input())
T = 1

for t in range(1, 1+T):
    N, M = list(map(int, input().split()))
    arr = [list(input()) for _ in range(N)]

    n = 0
    for i in range(N):


        for k in range(0, N-M+1):
            n = 0
            result = []
            while n < int(M/2):

                if arr[i][k+n] == arr[i][M+k-n-1]:
                    n += 1

                else:
                    break

            if n >= int(M/2):
                result = arr[i][k:k+M]
                break
        if n >= int(M / 2):
            break

    if not result:
        n = 0
        for k in range(0, N):



            for i in range(0, N - M + 1):
                n = 0
                result = []

                while n < int(M/2):
                    if arr[i+n][k] == arr[M+i-n-1][k]:
                        n += 1

                    else:
                        break

                if n >= int(M/2):
                    for j in range(i, i + M ):
                        result.append(arr[j][k])
                    break
            if n >= int(M / 2):
                break

    final =''
    for i in result:
        final += '{}'.format(i)

    print("#{} {}".format(t, final))

