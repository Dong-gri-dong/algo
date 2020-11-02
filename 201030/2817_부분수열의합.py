import sys
sys.stdin = open("input_data/2817_부분수열의합.txt")

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())

    arrs = list(map(int, input().split()))


    def powerset_sum(k, sums):
        global count
        if sums > K:
            return

        if k == N:
            if sums == K:
                count += 1
            return
        else:
            powerset_sum(k + 1, sums + arrs[k])
            powerset_sum(k + 1, sums)

    count = 0
    powerset_sum(0, 0)
    print('#{} {}'.format(test_case, count))

