import sys
import pprint
sys.stdin = open('input_data/4613.txt')


T = int(input())
T = 1

for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))

    a = [list(input()) for i in range(N)]

    pprint.pprint(a)

    count = 0

    # 처음에 


    for i in range(N):
        if i == 0:
            for k in a[i]:
                if k != 'W':
                    count += 1

        elif i == N-1:
            for k in a[i]:
                if k != 'R':
                    count += 1
        else:


            pass


