import sys

sys.stdin = open('input_data/4828.txt')

T = int(input())

for t in range(1, T + 1):
    num = int(input())
    numbers = list(map(int, input().split()))
    result_max = numbers[0]
    result_min = numbers[0]

    for i in range(num):
        if result_max < numbers[i]:
            result_max = numbers[i]

        elif result_min > numbers[i]:
            result_min = numbers[i]
    print('#{} {}'.format(t, result_max-result_min))


