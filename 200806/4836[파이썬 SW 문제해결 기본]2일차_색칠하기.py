import sys

sys.stdin = open('input_data/4836.txt')


T = int(input())

for t in range(1, T + 1):
    arr_num = int(input())


    arr = [[0 for j in range(10)] for i in range(10)]


    for _ in range(arr_num):
        arr_spec = list(map(int, input().split()))

        for i in range(arr_spec[0], arr_spec[2]+1):
            for n in range(arr_spec[1], arr_spec[3] + 1):
                if arr[i][n] != arr_spec[4] and arr[i][n] != 3:
                    arr[i][n] += arr_spec[4]
                #arr[i][n] = arr[i][n] + 1
    result = 0
    for i in range(10):
        for n in range(10):
            if arr[i][n] == 3:
                result += 1



    print('#{} {}'.format(t, result))


