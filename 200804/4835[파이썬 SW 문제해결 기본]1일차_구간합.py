import sys

sys.stdin = open('input_data/4835.txt')

T = int(input())

for t in range(1, T + 1):
    N, M  = list(map(int, input().split()))
    #N: 배열의 수 M : 이웃한 M개의 합

    number = list(map(int, input().split()))

    sum_lists = []
    for i in range(N-M+1):
        sum_lists.append(sum(number[i:i+M]))

    result_max =sum_lists[0]
    result_min = sum_lists[0]
    for n in number:
        if result_max < n:
            result_max = n

        elif result_min > n:
            result_min = n


    print('#{} {}'.format(t, max(sum_lists)-min(sum_lists)))





