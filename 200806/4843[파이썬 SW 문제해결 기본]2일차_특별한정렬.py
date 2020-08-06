import sys

sys.stdin = open('input_data/4843.txt')


T = int(input())

for t in range(1, T + 1):
    num = int(input())
    arr = list(map(int, input().split()))

    result = ''
    for i in range(num):

        if not i % 2 : #max
            max = 0 #arr[i]
            for n in range(i, num):
                if max <= arr[n]:
                    max = arr[n]
                    max_idx = n

            arr[i], arr[max_idx] = arr[max_idx], arr[i]

        else: #min
            min = 101#arr[i]
            for n in range(i, num):
                if min >= arr[n]:
                    min = arr[n]
                    min_idx = n
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    for i in range(10):
        result += ' {}'.format(arr[i])

    print('#{}{}'.format(t, result))


