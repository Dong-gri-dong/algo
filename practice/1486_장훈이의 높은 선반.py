import sys

sys.stdin = open("input_data/1486.txt")


# T = int(input())
#
#
# for test_case in range(1, T+1):
#     N, top = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#
#     def powerset(n, k, top):
#
#         if n == k:
#             sums = []
#             for i in range(n):
#                 if A[i]:
#                     sums.append(arr[i])
#             a = sum(sums)
#
#             if top <= a:
#
#                 keep.append(a)
#
#
#         else:
#             # k번째 선택
#             A[k] = 1
#             powerset(n, k + 1, top)
#             # k번째 비선택
#             A[k] = 0
#             powerset(n, k + 1, top)
#
#     N = len(arr)
#     A = [0] * N
#     keep = []
#     powerset(N, 0, top)
#
#
#     mins = keep[0]- top
#     for i in range(1, len(keep)):
#         if keep[i]- top <= mins:
#            mins = keep[i]- top
#
#
#     print('#{} {}'.format(test_case, mins))


def dfs(x, y):
    global result
    global N
    global E
    if x == N:
        if y >= E:
            result.append(y-E)
        return
    else:
        visited[x] = 1
        dfs(x + 1, y + temp[x])
        visited[x] = 0
        dfs(x + 1, y)


T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    temp = list(map(int, input().split()))
    result = []
    visited = [0] * N
    dfs(0, 0)
    print('#{} {}'.format(t, min(result)))
