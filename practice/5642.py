import sys

sys.stdin = open('input_data/5642.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    TC = list(map(int, input().split()))
    sum_list = TC[0]
    for i in range(1, len(TC)+1):
        for n in range(len(TC)-i):
            a = sum(TC[n:n + i])
            if sum_list < a:
                sum_list = a
    print('#{} {}'.format(t, sum_list))





