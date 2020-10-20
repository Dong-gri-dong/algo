import sys
import pprint

sys.stdin = open("input_data/1210.txt")

# T = 10
# for test_case in range(1, T + 1):
#     _ = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#
#     for i in range(100):
#         if arr[-1][i] == 2:
#             k = i
#     i = 100 - 1
#     while i != 0:
#
#         if k + 1 >= 100:
#             while arr[i][k - 1] == 1:
#                 k -= 1
#             i -= 1
#
#         elif k - 1 < 0:
#             while arr[i][k + 1] == 1:
#                 k += 1
#             i -= 1
#
#         else:
#             if arr[i][k + 1] == 1:
#                 k += 1
#                 while arr[i][k + 1] == 1:
#                     k += 1
#                     if k == 99:
#                         break
#                 i -= 1
#
#             elif arr[i][k - 1] == 1:
#                 k -= 1
#                 while arr[i][k - 1] == 1:
#                     k -= 1
#                     if k == 0:
#                         break
#                 i -= 1
#
#             else:
#                 i -= 1
#
#     print('#{} {}'.format(test_case, k))


#
#
# T = 10
# for test_case in range(1, T + 1):
#     _ = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#
#     for i in range(100):
#         if arr[-1][i] == 2:
#             k = i
#     i = 100 - 1
#     while i != 0:
#
#         if k + 1 >= 100:
#             while arr[i][k - 1] == 1:
#                 k -= 1
#             i -= 1
#
#         elif k - 1 < 0:
#             while arr[i][k + 1] == 1:
#                 k += 1
#             i -= 1
#
#         else:
#             if arr[i][k + 1] == 1:
#                 k += 1
#                 while arr[i][k + 1] == 1:
#                     k += 1
#                     if k == 99:
#                         break
#                 i -= 1
#
#             elif arr[i][k - 1] == 1:
#                 k -= 1
#                 while arr[i][k - 1] == 1:
#                     k -= 1
#                     if k == 0:
#                         break
#                 i -= 1
#
#             else:
#                 i -= 1
#
#     print('#{} {}'.format(test_case, k))

# 상 좌 우
dx = [ 0, -1, 1]
dy = [-1, 0, 0]
T = 1
for test_case in range(1, T + 1):
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    visit = [[0]*100 for _ in range(100)]

    for i in range(len(arr[99])):
        if arr[99][i] == 2:
            X = i

    def dfs(y, x):
        S = []
        S.append([y, x])
        visit[y][x] = 1
        while S:
            print(x)
            for i in range(3):
                tx = x + dx[i]
                ty = y + dy[i]

                if tx < 0 or tx == 100 or ty < 0 or ty == 100:
                    continue
                if arr[ty][tx] == 0 or visit[ty][tx] == 1:
                    continue

                S.append([y, x])
                visit[ty][tx] = 1
                x = tx
                y = ty

                if y == 0:
                    print(x)
                    return
                break
            else:
                y, x = S.pop()

    dfs(99, X)

    for i in visit:
        print(*i)