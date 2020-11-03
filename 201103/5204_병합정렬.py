import sys
sys.stdin = open("input_data/5204_병합정렬.txt")

T = int(input())

def merge_sort(Data):
    if len(Data) <= 1:
        return Data

    mid = len(Data) // 2
    left = merge_sort(Data[:mid])
    right = merge_sort(Data[mid:])
    return merge(left, right)


def merge(left, right):
    global count



    left_N = len(left)
    right_N = len(right)
    left_I = 0
    right_I = 0
    k = 0
    result = [0] * (left_N + right_N)

    if left[-1] > right[-1]:
        count += 1

    while left_I != left_N and right_I != right_N:
        if left[left_I] <= right[right_I]:
            result[k] += left[left_I]
            k += 1
            left_I += 1
        else:
            result[k] += right[right_I]
            k += 1
            right_I += 1

    if left_I != left_N:
        while left_I != left_N:
            result[k] += left[left_I]
            k += 1
            left_I += 1

    if right_I != right_N:
        while right_I != right_N:
            result[k] += right[right_I]
            k += 1
            right_I += 1


    return result




for test_case in range(1, T+1):

    N= int(input())
    arr = list(map(int, input().split()))
    count = 0
    arrs = merge_sort(arr)



    print('#{} {} {}'.format(test_case, arrs[N//2], count))