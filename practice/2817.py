import sys
import pprint
sys.stdin = open('input_data/2817.txt')

T = int(input())

for test_case in range(1, T+1):

    N, K = map(int, input().split())
    arr = list(map(int, input().split()))


    n = len(arr)
    total = 1 << n

    part = []
    count = 0
    for i in range(total):
        sums = 0
        for j in range(n):
            if i&(1<<j):
                sums += arr[j]

        if sums == K:
            count += 1

    print('#{} {}'.format(test_case, count))


