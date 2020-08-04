import sys

sys.stdin = open('input_data/1208.txt')


def maxs(x):
    result_max = x[0]
    result_idx = 0
    for idx, n in enumerate(x):
        if result_max < n:
            result_max = n
            result_idx = idx
    return result_max, result_idx


def mins(x):
    result_min = x[0]
    result_idx = 0
    for idx, n in enumerate(x):
        if result_min > n:
            result_min = n
            result_idx = idx
    return result_min, result_idx


T =10

for t in range(1, T + 1):
    dump = int(input())
    boxs = list(map(int, input().split()))

    for d in range(dump):
        maxs_, max_idx = maxs(boxs)
        mins_, min_idx = mins(boxs)
        # if maxs_ - mins_ <= 1:
        #     result = 0
        #     break

        boxs[max_idx] = boxs[max_idx] - 1
        boxs[min_idx] = boxs[min_idx] + 1

    max_boxs, _ = maxs(boxs)
    min_boxs, _ = mins(boxs)

    # if result:
    #     pass
    # else:
    result = max_boxs - min_boxs
    print('#{} {}'.format(t, result))


