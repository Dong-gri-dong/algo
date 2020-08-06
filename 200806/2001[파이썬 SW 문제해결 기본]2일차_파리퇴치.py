import sys

sys.stdin = open('input_data/2001.txt')


T = int(input())

for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    pari = 0
    arr =[list(map(int, input().split())) for _ in range(N)]

    paris = []
    for i in range(0, N-M+1):

        for n in range(0, N - M + 1):

            for k in range(M):
                for j in range(M):
                    pari += arr[i+k][n+j]
            paris.append(pari)
            pari = 0

    print('#{} {}'.format(t, max(paris)))


