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




T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if arr[-1][i] == 2:
            k = i
    i = 100 - 1
    while i != 0:

        if k + 1 >= 100:
            while arr[i][k - 1] == 1:
                k -= 1
            i -= 1

        elif k - 1 < 0:
            while arr[i][k + 1] == 1:
                k += 1
            i -= 1

        else:
            if arr[i][k + 1] == 1:
                k += 1
                while arr[i][k + 1] == 1:
                    k += 1
                    if k == 99:
                        break
                i -= 1

            elif arr[i][k - 1] == 1:
                k -= 1
                while arr[i][k - 1] == 1:
                    k -= 1
                    if k == 0:
                        break
                i -= 1

            else:
                i -= 1

    print('#{} {}'.format(test_case, k))
