import sys
import pprint
sys.stdin = open('input_data/1216.txt')

T = int(input())

for test_casre in range(1, T+1)




# def pal(arr):
#     return arr == arr[::-1]
# for t in range(1, 1+10):
#     _ = int(input())
#     N = 100
#     arr = [input() for _ in range(N)]
#     count = 1
#     for i in range(N):
#         for k in range(N):
#             j = 0
#             x = ''
#             y = ''
#             if N-k > count:
#                 while k+j < 100 :
#                     x += arr[i][k + j]
#                     y += arr[k + j][i]
#                     if pal(x):
#                         if len(x) > count:
#                             count = len(x)
#                     if pal(y):
#                         if len(y) > count:
#                             count = len(y)
#                     j += 1
#     print('#{} {}'.format(t, count))


#
#
# for test_case in range(10):
#     length = 100
#     T = int(input())
#     str_list = [input() for _ in range(length)]
#
#     isFinished = False
#
#     max_lenPattern = 0
#     for lenPattern in range(length, 0, -1):
#         for i in range(length):
#             for j in range(length + 1 - lenPattern):
#                 for k in range(lenPattern // 2):
#                     if str_list[i][j + k] != str_list[i][j + lenPattern - k - 1]:
#                         break
#                 else:
#                     isFinished = True
#                     max_lenPattern = lenPattern
#                     break
#
#             for j in range(length + 1 - lenPattern):
#                 for k in range(lenPattern // 2):
#                     if str_list[j + k][i] != str_list[j + lenPattern - k - 1][i]:
#                         break
#                 else:
#                     isFinished = True
#                     max_lenPattern = lenPattern
#                     break
#             if isFinished: break
#         if isFinished: break
#
#     print('#{} {}'.format(test_case + 1, max_lenPattern))



