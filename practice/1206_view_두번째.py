import sys
sys.stdin = open("input_data/1206.txt")


def views(arr):



    if arr[2] == max(arr):

        return arr[2] -max((arr[0:2]) + arr[3:5])
    else:
        return 0

for test_case in range(1, 11):
    n = int(input())
    arrs = list(map(int, input().split()))
    #
    sum = 0
    for i in range(2, len(arrs)-2):
        sum += views(arrs[i-2:i+3])

    print('#{} {}'.format(test_case, sum))
