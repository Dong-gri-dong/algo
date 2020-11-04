import sys
sys.stdin = open("input_data/4466_최대성적표만들기.txt")


T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # def score(k, sums, s):
    #
    #     global result
    #     if len(sums) > K:
    #         return
    #     if k == N:
    #         if len(sums) == K:
    #             if result <= s:
    #                 result = s
    #         return
    #
    #     else:
    #
    #         score(k + 1, sums + [arr[k]], s+arr[k])
    #         score(k + 1, sums, s)
    # result = 0
    # score(0, [], 0)


    result = sum(sorted(arr, reverse=True)[:K])

    print('#{} {}'.format(test_case, result))