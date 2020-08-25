import sys
import pprint
sys.stdin = open('input_data/4613.txt')


T = int(input())

# for test_case in range(1, T + 1):
#     N, M = list(map(int, input().split()))
#     arr = [list(input()) for i in range(N)]
#     count = 0
#     mins = []
#     for i in range(0, N - 3 + 1):
#         for j in range(i + 1, N - 2 + 1):
#             count = 0
#             for k in range(len(arr[:i + 1])):
#                 for u in arr[:i + 1][k]:
#                     if 'W' != u:
#                         count += 1
#
#             for k in range(len(arr[i + 1:j + 1])):
#                 for u in arr[i + 1:j + 1][k]:
#                     if 'B' != u:
#                         count += 1
#
#             for k in range(len(arr[j + 1:])):
#                 for u in arr[j + 1:][k]:
#                     if 'R' != u:
#                         count += 1
#
#             mins.append(count)
#     print('#{} {}'.format(test_case,  min(mins)))


T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(input()) for i in range(N)]
    count = 0
    mins = []
    top_down = 0
    for u in arr[0]:
        if 'W' != u:
            top_down += 1
    for u in arr[-1]:
        if 'R' != u:
            top_down += 1


    for i in range(1, N-1):
        for j in range(i, N - 1):
            count = 0
            for k in range(len(arr[1 : i])):
                for u in arr[1 : i][k]:
                    if 'W' != u:
                        count += 1
            for k in range(len(arr[i :j + 1])):
                for u in arr[i :j + 1][k]:
                    if 'B' != u:
                        count += 1

            for k in range(len(arr[j + 1 : N-1])):
                for u in arr[j + 1 : N-1][k]:
                    if 'R' != u:
                        count += 1
            mins.append(count)

    print('#{} {}'.format(test_case,  min(mins)+top_down))

# T = int(input())
# for t in range(T):
#     N, M = map(int, input().split())
#     origin = []
#     for n in range(N):
#         row = list(input())
#         # 각 행의 W, B. R 개수를 미리 세서 저장
#         row.append(row.count('W'))
#         row.append(row.count('B'))
#         row.append(row.count('R'))
#         origin.append(row)
#
#     mini = N * M
#     for i in range(0, N - 2):
#         for j in range(i + 1, N - 1):
#             # 다시 색칠하지 않아도 되는 칸의 개수를 right에 저장
#             right = 0
#             for a in range(N):
#                 if 0 <= a <= i:
#                     right += origin[a][M]
#                 elif i < a <= j:
#                     right += origin[a][M + 1]
#                 else:
#                     right += origin[a][M + 2]
#             if mini > N * M - right:
#                 mini = N * M - right
#     print('#{} {}'.format(t + 1, mini))